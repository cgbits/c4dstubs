from __future__ import annotations

import os
import ast

from typing import Any, Callable, Generator, List, Dict, Optional, Tuple
from pathlib import Path


class ConstantDef:
    def __init__(self, name: str) -> None:
        self.name = name

    def render(self) -> str:
        return f"{self.name}: int = ...\n"


class HintDef:
    def __init__(self, name: str, children: Optional[List[HintDef]] = None):
        if children is None:
            children = []

        self.name = name
        self.children = children

    def render(self) -> str:
        children = self.children
        children_string = ""

        name = self.name

        if self.children:
            if name == "Dict" and len(children) > 2:
                children = children[:2]
            elif name == "List" and len(children) > 1:
                children = children[:1]

            children_string = (
                "[" + ", ".join([x.render() for x in children]) + "]"
            )
        else:
            if name == "Dict":
                children_string = "[str, Any]"

            elif name == "List":
                children_string = "[Any]"

        return name + children_string

    def iterate_children(self) -> Generator[HintDef, None, None]:
        yield self

        for child in self.children:
            yield from child.iterate_children()


class ArgumentDef:
    def __init__(
        self,
        name: str,
        hint: Optional[HintDef] = None,
        has_default: bool = False,
        default: Optional[str] = None,
    ):
        self.name = name
        self.hint = hint
        self.has_default = has_default
        self.default = default

    def render(self) -> str:
        result = self.name

        if self.name == "self":
            return result

        if self.hint:
            result += ": " + self.hint.render()
        else:
            result += ": Any"

        if self.has_default:
            result += " = " + str(self.default)

        return result


class FunctionDef:
    def __init__(
        self,
        name: str,
        arguments: Optional[List[ArgumentDef]] = None,
        return_type: Optional[HintDef] = None,
        comment: Optional[str] = None,
    ):
        if arguments is None:
            arguments = []

        self.name = name
        self.arguments = arguments
        self.return_type = return_type
        self.comment = comment

    def render(self) -> str:
        result = "def " + self.name

        result += "("

        result += ", ".join([x.render() for x in self.arguments])

        return_type = (
            self.return_type.render() if self.return_type else str(None)
        )

        if self.name == "__init__":
            return_type = "None"

        result += ") -> " + return_type + ":\n"

        if self.comment:
            comment = self.comment.replace("\\", "\\\\")
            result += " " * 4 + '"""' + "\n"
            result += "\n".join([" " * 4 + x for x in comment.split("\n")])
            result += "\n" + " " * 4 + '"""' + "\n"

        result += " " * 4 + "...\n"

        return result

    def get_hints(self) -> List[HintDef]:
        hints: List[HintDef] = []

        for argument in self.arguments:
            if argument.hint:
                hints.append(argument.hint)

        if self.return_type:
            hints.append(self.return_type)

        return hints


class ClassDef:
    def __init__(
        self,
        name: str,
        bases: Optional[List[str]] = None,
        functions: Optional[List[FunctionDef]] = None,
        attributes: Optional[List[ArgumentDef]] = None,
    ) -> None:
        self.name = name
        self.bases = bases
        self.functions = functions
        self.attributes = attributes

    def render(self) -> str:
        result = "class " + self.name

        if self.bases:
            result += "("

            result += ", ".join(self.bases)

            result += ")"

        result += ":\n"

        if self.attributes:
            for attribute in self.attributes:
                result += " " * 4 + attribute.render() + "\n"

        if self.functions:
            result += "\n"

            for function in self.functions:
                if function.arguments:
                    if function.arguments[0].name != "self":
                        result += " " * 4 + "@staticmethod\n"
                else:
                    result += " " * 4 + "@staticmethod\n"

                result += "\n".join(
                    [" " * 4 + x for x in function.render().split("\n")]
                )

                result += "\n"

        if not self.attributes and not self.functions:
            result += " " * 4 + "...\n"

        return result

    def get_hints(self) -> List[HintDef]:
        hints: List[HintDef] = []

        if self.functions:
            for function in self.functions:
                hints += function.get_hints()

        return hints


def parse_hint(hint: str) -> HintDef:
    illegal_hint_names = ["Slice", "buffer", "active", "multi"]

    hint = hint.strip()

    if not hint:
        raise Exception("Hint must not be empty")

    if hint.startswith("function"):
        return HintDef("Callable[..., Any]")

    hint = hint.replace("(", "[").replace(")", "]")

    hint = hint.replace("{", "[").replace("}", "]")

    hint = hint.replace("*", "")

    hint = hint.replace("<", "").replace(">", "")

    hint = hint.replace("`", "")

    opening_bracket_index = hint.find("[")
    closing_bracket_index = hint[::-1].find("]")

    if opening_bracket_index > -1 or closing_bracket_index > -1:
        # we have opening and or closing brackets
        if opening_bracket_index > -1 and closing_bracket_index > -1:
            # opening and closing brackets are present
            start = opening_bracket_index + 1
            stop = len(hint) - closing_bracket_index - 1

            substring = hint[start:stop]

            children: List[HintDef] = []

            for child in filter(
                bool, [x.strip() for x in substring.split(",")]
            ):
                try:
                    children.append(parse_hint(child))
                except Exception:
                    pass

            hint_instance = parse_hint(hint[: start - 1])

            hint_instance.children = children

            return hint_instance
        else:
            raise Exception(f"Missing bracket counterpart in {hint}")
    elif " " in hint:
        raise Exception("Hint must not contain space")
    elif hint in illegal_hint_names:
        raise Exception(f"Hint must not be {hint}")
    elif "maxon" in hint:
        raise Exception("Value 'maxon' is not allowed in hint")
    else:
        if hint.startswith("dict"):
            hint = hint.replace("dict", "Dict")

        if hint.startswith("list"):
            hint = hint.replace("list", "List")

        if hint.startswith("tuple"):
            hint = hint.replace("tuple", "Tuple")

        if hint.startswith("any"):
            hint = hint.replace("any", "Any")

        if hint == "PyCObject":
            hint = "Any"

        if hint == "number":
            hint = "float"

        if hint == "long":
            hint = "int"

        if hint == "16float":
            hint = "float"

        if hint == "intcl":
            hint = "int"

        if hint == "ptr":
            hint = "Any"

        if hint == "Object":
            hint = "object"

        if hint == "Type":
            hint = "Any"

        if hint == "string":
            hint = "str"

        if hint.lower() == "true":
            hint = "bool"

        if hint.lower() == "false":
            hint = "bool"

        if hint.endswith("."):
            hint = hint[:-1]

        # no opening or closing brackets are present
        return HintDef(hint)

    # raise Exception(f"No hint could be parsed from {hint}")


def parse_type(type_string: str) -> Tuple[Optional[str], HintDef]:
    parts = list(filter(bool, [x.strip() for x in type_string.split(":")]))

    if len(parts) == 2:
        hint_result = parse_hint(parts[1])

        if parts[0].startswith("type "):
            # parse hint
            return (parts[0].replace("type ", ""), hint_result)
        elif parts[0].startswith("rtype"):
            # parse hint
            return (None, hint_result)

    raise Exception(f"No type hint could be parsed from {type_string}")


def prepare_function(node: ast.FunctionDef) -> FunctionDef:
    arguments: List[ArgumentDef] = [ArgumentDef(x.arg) for x in node.args.args]
    argument_names: List[str] = [x.name for x in arguments]
    comment: Optional[str] = None

    return_type = HintDef("None")

    # parse comment
    for body_node in node.body:
        if isinstance(body_node, ast.Expr):
            if isinstance(body_node.value, ast.Str):
                comment = body_node.value.s

                comment_lines = comment.split("\n")

                for line in comment_lines:
                    line_stripped = line.strip()

                    try:
                        argument_name, hint = parse_type(line_stripped)

                        if argument_name in argument_names:
                            arguments[
                                argument_names.index(argument_name)
                            ].hint = hint
                        else:
                            return_type = hint
                    except Exception:
                        pass

                comment = "\n".join(
                    filter(bool, [x.strip() for x in comment_lines])
                )

                break

    function_definition = FunctionDef(
        node.name, arguments, return_type, comment
    )

    return function_definition


def prepare_class(node: ast.ClassDef) -> ClassDef:
    class_name = node.name

    bases: List[str] = []

    for expression in node.bases:
        if isinstance(expression, ast.Name):
            bases.append(expression.id)

    # get all class functions
    function_definitionns: List[FunctionDef] = []

    for body_node in node.body:
        if isinstance(body_node, ast.FunctionDef):
            try:
                function_definitionns.append(prepare_function(body_node))
            except Exception:
                pass

    class_definition = ClassDef(class_name, bases, function_definitionns)

    return class_definition


def parse_stubs(
    file: Path,
) -> Dict[str, Any]:
    constants: List[ConstantDef] = []

    classes: List[ClassDef] = []

    functions: List[FunctionDef] = []

    with open(file, "r") as src:
        tree = ast.parse(src.read())

        for node in tree.body:
            class_names = [x.name for x in classes]
            function_names = [x.name for x in functions]

            if isinstance(node, ast.AnnAssign):
                if isinstance(node.target, ast.Name):
                    constants.append(ConstantDef(node.target.id))
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        constants.append(ConstantDef(target.id))
            elif isinstance(node, ast.ClassDef):
                try:
                    class_definition = prepare_class(node)

                    if class_definition.name not in class_names:
                        classes.append(class_definition)
                except Exception:
                    pass
            elif isinstance(node, ast.FunctionDef):
                try:
                    function_definition = prepare_function(node)

                    if function_definition.name not in function_names:
                        functions.append(function_definition)
                except Exception:
                    pass

    return {"constants": constants, "classes": classes, "functions": functions}


def module_path_from_file(path: Path) -> str:
    filename = os.path.splitext(path.name)[0]

    if filename == "__init__":
        return str(path.parent).replace("/", ".")
    else:
        return str(path.parent.joinpath(filename)).replace("/", ".")


if __name__ == "__main__":
    src_directory = Path(os.path.join(os.path.dirname(__file__), "src"))

    package_directory = src_directory.joinpath("c4d")

    destination_directory = Path(
        os.path.join(os.path.dirname(__file__), "dist")
    )

    modules: Dict[str, Any] = {}

    class_overrides: List[ClassDef] = [
        ClassDef(
            "Matrix",
            functions=[
                FunctionDef(
                    "__init__",
                    [
                        ArgumentDef("self"),
                        ArgumentDef(
                            "off",
                            HintDef("Optional", [HintDef("Vector")]),
                            True,
                            "...",
                        ),
                        ArgumentDef(
                            "v1",
                            HintDef("Optional", [HintDef("Vector")]),
                            True,
                            "...",
                        ),
                        ArgumentDef(
                            "v2",
                            HintDef("Optional", [HintDef("Vector")]),
                            True,
                            "...",
                        ),
                        ArgumentDef(
                            "v3",
                            HintDef("Optional", [HintDef("Vector")]),
                            True,
                            "...",
                        ),
                    ],
                ),
            ],
            attributes=[
                ArgumentDef("off", HintDef("Vector")),
                ArgumentDef("v1", HintDef("Vector")),
                ArgumentDef("v2", HintDef("Vector")),
                ArgumentDef("v3", HintDef("Vector")),
            ],
        ),
        ClassDef(
            "Vector",
            functions=[
                FunctionDef(
                    "__init__",
                    [
                        ArgumentDef("self"),
                        ArgumentDef(
                            "x",
                            HintDef(
                                "Optional",
                                [
                                    HintDef(
                                        "Union",
                                        [
                                            HintDef("int"),
                                            HintDef("Vector"),
                                            HintDef("float"),
                                        ],
                                    )
                                ],
                            ),
                            True,
                            "...",
                        ),
                        ArgumentDef(
                            "y",
                            HintDef(
                                "Optional",
                                [
                                    HintDef(
                                        "Union",
                                        [HintDef("int"), HintDef("float")],
                                    )
                                ],
                            ),
                            True,
                            "...",
                        ),
                        ArgumentDef(
                            "z",
                            HintDef(
                                "Optional",
                                [
                                    HintDef(
                                        "Union",
                                        [HintDef("int"), HintDef("float")],
                                    )
                                ],
                            ),
                            True,
                            "...",
                        ),
                    ],
                ),
                FunctionDef(
                    "__mul__",
                    [
                        ArgumentDef("self"),
                        ArgumentDef(
                            "other",
                            HintDef(
                                "Union",
                                [
                                    HintDef("Matrix"),
                                    HintDef("Vector"),
                                    HintDef("float"),
                                ],
                            ),
                        ),
                    ],
                    HintDef("Vector"),
                ),
            ],
            attributes=[
                ArgumentDef("x", HintDef("float")),
                ArgumentDef("y", HintDef("float")),
                ArgumentDef("z", HintDef("float")),
            ],
        ),
        ClassDef(
            "GvNode",
            functions=[
                FunctionDef(
                    "AddPort",
                    [
                        ArgumentDef("self"),
                        ArgumentDef("io", HintDef("int")),
                        ArgumentDef(
                            "id",
                            HintDef(
                                "Union", [HintDef("int"), HintDef("DescID")]
                            ),
                        ),
                        ArgumentDef(
                            "flag",
                            HintDef("Optional", [HintDef("int")]),
                            True,
                            "...",
                        ),
                        ArgumentDef(
                            "message",
                            HintDef("Optional", [HintDef("bool")]),
                            True,
                            "...",
                        ),
                    ],
                    HintDef("GvPort"),
                )
            ],
        ),
        ClassDef(
            "GvNodeMaster",
            functions=[
                FunctionDef(
                    "CreateNode",
                    [
                        ArgumentDef("self"),
                        ArgumentDef("parent", HintDef("GvNode")),
                        ArgumentDef("id", HintDef("int")),
                        ArgumentDef(
                            "insert",
                            HintDef("Optional", [HintDef("GvNode")]),
                            True,
                            "...",
                        ),
                        ArgumentDef(
                            "x",
                            HintDef("Optional", [HintDef("int")]),
                            True,
                            "...",
                        ),
                        ArgumentDef(
                            "y",
                            HintDef("Optional", [HintDef("int")]),
                            True,
                            "...",
                        ),
                    ],
                    HintDef("GvNode"),
                )
            ],
        ),
        ClassDef(
            "BaseContainer",
            functions=[
                FunctionDef(
                    "__init__",
                    [
                        ArgumentDef("self"),
                        ArgumentDef(
                            "n",
                            HintDef(
                                "Optional",
                                [
                                    HintDef(
                                        "Union",
                                        [
                                            HintDef("BaseContainer"),
                                            HintDef("int"),
                                        ],
                                    )
                                ],
                            ),
                            True,
                            "...",
                        ),
                    ],
                )
            ],
        ),
        ClassDef(
            "DescID",
            functions=[
                FunctionDef(
                    "__init__",
                    [
                        ArgumentDef("self"),
                        ArgumentDef("id1", HintDef("DescLevel")),
                        ArgumentDef(
                            "id2",
                            HintDef("Optional", [HintDef("DescLevel")]),
                            True,
                            "...",
                        ),
                        ArgumentDef(
                            "id3",
                            HintDef("Optional", [HintDef("DescLevel")]),
                            True,
                            "...",
                        ),
                    ],
                )
            ],
        ),
        ClassDef(
            "DescLevel",
            functions=[
                FunctionDef(
                    "__init__",
                    [
                        ArgumentDef("self"),
                        ArgumentDef("t_id", HintDef("int")),
                        ArgumentDef(
                            "t_datatype",
                            HintDef("Optional", [HintDef("int")]),
                            True,
                            "...",
                        ),
                        ArgumentDef(
                            "t_creator",
                            HintDef("Optional", [HintDef("int")]),
                            True,
                            "...",
                        ),
                    ],
                )
            ],
        ),
        ClassDef(
            "GeListNode",
            functions=[
                FunctionDef(
                    "GetChildren",
                    [ArgumentDef("self")],
                    HintDef("List", [HintDef("GeListNode")]),
                ),
                FunctionDef(
                    "GetDataInstance",
                    [ArgumentDef("self")],
                    HintDef("BaseContainer"),
                ),
            ],
        ),
        ClassDef(
            "BaseList2D",
            functions=[
                FunctionDef(
                    "GetChildren",
                    [ArgumentDef("self")],
                    HintDef("List", [HintDef("BaseList2D")]),
                ),
                FunctionDef(
                    "SetLayerObject",
                    [
                        ArgumentDef("self"),
                        ArgumentDef(
                            "layer",
                            HintDef("Optional", [HintDef("LayerObject")]),
                        ),
                    ],
                ),
            ],
        ),
        ClassDef(
            "BaseObject",
            functions=[
                FunctionDef(
                    "GetChildren",
                    [ArgumentDef("self")],
                    HintDef("List", [HintDef("BaseObject")]),
                ),
                FunctionDef(
                    "MakeTag",
                    [
                        ArgumentDef("self"),
                        ArgumentDef("x", HintDef("int")),
                        ArgumentDef(
                            "pred",
                            HintDef("Optional", [HintDef("BaseTag")]),
                            True,
                            "...",
                        ),
                    ],
                    HintDef("BaseTag"),
                ),
                FunctionDef(
                    "InsertTag",
                    [
                        ArgumentDef("self"),
                        ArgumentDef("tp", HintDef("BaseTag")),
                        ArgumentDef(
                            "pred",
                            HintDef("Optional", [HintDef("BaseTag")]),
                            True,
                            "...",
                        ),
                    ],
                    HintDef("BaseTag"),
                ),
            ],
        ),
        ClassDef(
            "PriorityData",
            functions=[
                FunctionDef(
                    "__init__",
                    [
                        ArgumentDef("self"),
                        ArgumentDef(
                            "v",
                            HintDef("Optional", [HintDef("PriorityData")]),
                            True,
                            "...",
                        ),
                    ],
                )
            ],
        ),
        ClassDef(
            "TagData",
            functions=[
                FunctionDef(
                    "Message",
                    [
                        ArgumentDef("self"),
                        ArgumentDef("node", HintDef("BaseTag")),
                        ArgumentDef("type", HintDef("int")),
                        ArgumentDef("data", HintDef("Any")),
                    ],
                    HintDef("bool"),
                )
            ],
        ),
        ClassDef(
            "BaseDraw",
            functions=[
                FunctionDef(
                    "SetPen",
                    [
                        ArgumentDef("self"),
                        ArgumentDef("col", HintDef("Vector")),
                        ArgumentDef(
                            "flags",
                            HintDef("Optional", [HintDef("int")]),
                            True,
                            "...",
                        ),
                    ],
                )
            ],
        ),
        ClassDef(
            "BaseBitmap",
            functions=[
                FunctionDef(
                    "InitWith",
                    [
                        ArgumentDef("self"),
                        ArgumentDef(
                            "name",
                            HintDef(
                                "Union",
                                [HintDef("str"), HintDef("MemoryFileStruct")],
                            ),
                        ),
                        ArgumentDef(
                            "frame",
                            HintDef("Optional", [HintDef("int")]),
                            True,
                            "...",
                        ),
                    ],
                    HintDef("Tuple", [HintDef("int"), HintDef("bool")]),
                )
            ],
        ),
    ]

    class_overrides_names: List[str] = [x.name for x in class_overrides]

    function_overrides: List[FunctionDef] = [
        FunctionDef(
            "LoadDocument",
            [
                ArgumentDef(
                    "name",
                    HintDef(
                        "Union", [HintDef("str"), HintDef("MemoryFileStruct")]
                    ),
                ),
                ArgumentDef("loadflags", HintDef("int")),
                ArgumentDef(
                    "thread",
                    HintDef("Optional", [HintDef("BaseThread")]),
                    True,
                    "...",
                ),
            ],
        ),
        FunctionDef(
            "RegisterTagPlugin",
            [
                ArgumentDef("id", HintDef("int")),
                ArgumentDef("str", HintDef("str")),
                ArgumentDef("info", HintDef("int")),
                ArgumentDef("g", HintDef("Any")),
                ArgumentDef("description", HintDef("str")),
                ArgumentDef(
                    "icon",
                    HintDef("Optional", [HintDef("BaseBitmap")]),
                    True,
                    "...",
                ),
                ArgumentDef(
                    "disklevel",
                    HintDef("Optional", [HintDef("int")]),
                    True,
                    "...",
                ),
                ArgumentDef(
                    "res",
                    HintDef("Optional", [HintDef("GeResource")]),
                    True,
                    "...",
                ),
            ],
            HintDef("bool"),
        ),
    ]

    function_override_names: List[str] = [x.name for x in function_overrides]

    for root, _, filenames in os.walk(package_directory):
        root_path = Path(root)

        for filename in filenames:
            file = root_path.joinpath(filename)

            destination = destination_directory.joinpath(
                file.relative_to(src_directory)
            )

            if not destination.parent.is_dir():
                os.makedirs(destination.parent, mode=0o777, exist_ok=True)

            module_path = module_path_from_file(
                file.relative_to(src_directory)
            )

            modules[module_path] = {
                "destination": destination,
                "stubs": parse_stubs(file),
            }

    classes: Dict[str, str] = {}

    for module_path, module in modules.items():
        stubs = module["stubs"]

        for class_definition in stubs["classes"]:
            classes[class_definition.name] = module_path

    for module_path, module in modules.items():
        imports: Dict[str, List[str]] = {}
        stubs = module["stubs"]

        constant_definitions: List[ConstantDef] = stubs["constants"]
        class_definitions: List[ClassDef] = stubs["classes"]
        function_definitions: List[FunctionDef] = stubs["functions"]

        # apply class overrides
        for override_class_definition in class_definitions:
            if override_class_definition.name in class_overrides_names:
                class_override = class_overrides[
                    class_overrides_names.index(override_class_definition.name)
                ]

                functions: List[FunctionDef] = []

                if override_class_definition.functions:
                    functions = override_class_definition.functions

                if class_override.functions:
                    for function in class_override.functions:
                        function_names: List[str] = [x.name for x in functions]

                        if function.name in function_names:
                            # override
                            index = function_names.index(function.name)
                            original = functions[index]

                            function.comment = original.comment

                            functions[index] = function
                        else:
                            functions.append(function)

                attributes: List[ArgumentDef] = []

                if override_class_definition.attributes:
                    attributes = override_class_definition.attributes

                if class_override.attributes:
                    attributes += class_override.attributes

                override_class_definition.functions = functions
                override_class_definition.attributes = attributes

        # apply function overrides
        for override_function_definition in function_definitions:
            if override_function_definition.name in function_override_names:
                function_override = function_overrides[
                    function_override_names.index(
                        override_function_definition.name
                    )
                ]

                override_function_definition.arguments = (
                    function_override.arguments
                )
                override_function_definition.return_type = (
                    function_override.return_type
                )

        # collect imports from classes
        for import_class_definition in class_definitions:
            # collect imports from class bases
            if import_class_definition.bases:
                bases: List[str] = []

                if import_class_definition.bases:
                    for base in import_class_definition.bases:
                        parts = base.split(".")

                        class_name = parts[-1]

                        if class_name in classes:
                            class_names = imports.setdefault(
                                classes[class_name], []
                            )

                            if class_name not in class_names:
                                class_names.append(class_name)

                            bases.append(class_name)
                        else:
                            bases.append(base)

                import_class_definition.bases = bases

            # collect imports from argument hints
            hints = import_class_definition.get_hints()

            for hint in hints:
                for nhint in hint.iterate_children():
                    parts = nhint.name.split(".")

                    class_name = parts[-1]

                    if class_name in classes:
                        class_names = imports.setdefault(
                            classes[class_name], []
                        )

                        if class_name not in class_names:
                            class_names.append(class_name)

                        nhint.name = class_name
                    elif class_name.upper() == "UUID":
                        class_name = "UUID"

                        class_names = imports.setdefault("uuid", [])

                        if class_name not in class_names:
                            class_names.append(class_name)

                        nhint.name = class_name

        # collect imports from functions
        for import_function_definition in function_definitions:
            # collect imports from argument hints
            hints = import_function_definition.get_hints()

            for hint in hints:
                for nhint in hint.iterate_children():
                    parts = nhint.name.split(".")

                    class_name = parts[-1]

                    if class_name in classes:
                        class_names = imports.setdefault(
                            classes[class_name], []
                        )

                        if class_name not in class_names:
                            class_names.append(class_name)

                        nhint.name = class_name

        with open(module["destination"], "w") as f:
            # write default imports
            f.write("from __future__ import annotations\n")
            f.write(
                "from typing import Tuple, Union, Dict, List, Any, Optional, Iterable, Callable\n\n"
            )

            if module_path == "c4d":
                f.write("from c4d.symbols import *\n")
                # f.write(
                #     "from c4d import documents, gui, modules, plugins, storage, threading, utils, bitmaps\n"
                # )

            submodule_imports: List[str] = []

            for current_module_path in modules.keys():
                if current_module_path.startswith(module_path):
                    if len(current_module_path.split(".")) - 1 == len(
                        module_path.split(".")
                    ):
                        submodule_imports.append(
                            current_module_path.split(".")[-1]
                        )

            if submodule_imports:
                f.write("from . import " + ", ".join(submodule_imports) + "\n")

            # write imports
            for module_name, class_names in imports.items():
                if module_name != module_path:
                    f.write(
                        f"from {module_name} import "
                        + str(", ".join(class_names))
                        + "\n"
                    )

            # write constants
            if constant_definitions:
                for constant_definition in constant_definitions:
                    f.write(constant_definition.render())

            # write classes
            if class_definitions:
                for class_definition in class_definitions:
                    f.write("\n\n")
                    f.write(class_definition.render())

            # write functions
            if function_definitions:
                for function_definition in function_definitions:
                    f.write("\n\n")
                    f.write(function_definition.render())
