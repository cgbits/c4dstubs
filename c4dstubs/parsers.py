from __future__ import annotations

import os
import ast
import yaml

from pathlib import Path
from typing import List, Dict, Any, Optional, Union, Tuple
from c4dstubs.definitions import (
    ClassDef,
    ConstantDef,
    FunctionDef,
    ArgumentDef,
    HintDef,
)


def parse_hint(hint: str) -> HintDef:
    illegal_separator_characters = [" ", ","]
    illegal_characters = ["*", "`"]

    # strip whitespace around hint
    hint = hint.strip()

    # test for empty hint
    if not hint:
        raise Exception("Hint must not be empty")

    # test for illegal separator characters
    if "[" not in hint:
        for illegal_character in illegal_separator_characters:
            if illegal_character in hint:
                raise Exception(
                    f"Illegal character '{illegal_character}' found in hint '{hint}'"
                )

    # test for illegal characters
    for illegal_character in illegal_characters:
        if illegal_character in hint:
            raise Exception(
                f"Illegal character '{illegal_character}' found in hint '{hint}'"
            )

    # handle known case conversions
    replace: Dict[str, str] = {
        "any": "Any",
        "tuple": "Tuple",
        "optional": "Optional",
        "dict": "Dict",
        "number": "float",
        "list": "List",
        "long": "int",
        "PyCObject": "Any",
        "Object": "object",
        "16float": "float",
        "Type": "Any",
        "string": "str",
        "false": "bool",
        "true": "bool",
    }

    for key, value in replace.items():
        hint = hint.replace(key, value)

    # handle nested definitions in brackets
    opening_bracket_index = hint.find("[")
    closing_bracket_index = hint[::-1].find("]")

    if opening_bracket_index > -1 or closing_bracket_index > -1:
        # we have opening and or closing brackets
        if opening_bracket_index > -1 and closing_bracket_index > -1:
            # opening and closing brackets are present
            start = opening_bracket_index + 1
            stop = len(hint) - closing_bracket_index - 1

            substring = hint[start:stop]

            hint_instance = parse_hint(hint[: start - 1])

            if "[" in substring:
                hint_instance.children = [parse_hint(substring)]
            else:
                hint_instance.children = [
                    parse_hint(x) for x in substring.split(",")
                ]

            # post nested hints check
            if hint_instance.name == "Dict":
                if len(hint_instance.children) != 2:
                    raise Exception(
                        f"Number of nested definitions in Dict must be exactly 2, got {hint}"
                    )
            elif hint_instance.name == "List":
                if len(hint_instance.children) != 1:
                    raise Exception(
                        f"Number of nested definitions in List must be exactly 1, got {hint}"
                    )
            elif hint_instance.name == "Tuple":
                if not len(hint_instance.children) > 0:
                    raise Exception(
                        f"Number of nested definitions in Tuple must be larger 0, got {hint}"
                    )
            elif hint_instance.name == "Optional":
                if len(hint_instance.children) != 1:
                    raise Exception(
                        f"Number of nested definitions in Optional must be exactly 1, got {hint}"
                    )

            return hint_instance
        else:
            raise Exception(f"Missing bracket counterpart in {hint}")
    else:
        # no opening or closing brackets are present
        return HintDef(hint)


def parse_override_function_definition(
    name: str, definitions: Dict[str, str]
) -> FunctionDef:
    arguments: List[ArgumentDef] = []
    return_type: Optional[HintDef] = None

    for key, value in definitions.items():
        if key == "self":
            arguments.append(ArgumentDef("self"))

            continue
        elif key == "->":
            return_type = parse_hint(value)

            continue
        else:
            hint = value
            has_default = False
            default: Optional[str] = None

            if "=" in value:
                has_default = True
                default = "..."
                hint = value.split("=")[0]

            arguments.append(
                ArgumentDef(key, parse_hint(hint), has_default, default)
            )

    return FunctionDef(name, arguments, return_type)


def parse_override_argument_definition(
    name: str, definition: str
) -> ArgumentDef:
    return ArgumentDef(name, parse_hint(definition))


def parse_override(
    name: str, override: Union[Dict[str, str], str]
) -> Union[FunctionDef, ArgumentDef]:
    if isinstance(override, dict):
        argument_definitions: Dict[str, str] = override

        return parse_override_function_definition(name, argument_definitions)
    else:
        argument_definition: str = override

        return parse_override_argument_definition(name, argument_definition)


def parse_hint_with_fallback(
    definition: str, comment: Optional[str] = None
) -> Tuple[HintDef, int]:
    hint: Optional[HintDef] = None
    attempts: int = 0

    while hint is None:
        try:
            hint = parse_hint(definition)
        except Exception as e:
            print(e)

            if comment:
                print(comment)

            definition = input("Override with: ")

            attempts += 1

    return (hint, attempts)


def parse_function(node: ast.FunctionDef) -> Tuple[FunctionDef, bool]:
    requires_override: bool = False
    arguments: List[ArgumentDef] = [ArgumentDef(x.arg) for x in node.args.args]
    argument_names: List[str] = [x.name for x in arguments]
    comment: Optional[str] = None
    function_name = node.name

    return_type = HintDef("None")

    # parse comment
    for body_node in node.body:
        if isinstance(body_node, ast.Expr):
            if isinstance(body_node.value, ast.Str):
                comment = body_node.value.s

                comment_lines = comment.split("\n")

                # parse every line for potential type hints
                for line in comment_lines:
                    line_stripped = line.strip()

                    parts = list(
                        filter(
                            bool, [x.strip() for x in line_stripped.split(":")]
                        )
                    )

                    if len(parts) == 2:
                        if parts[0].startswith("type") or parts[0].startswith(
                            "rtype"
                        ):
                            hint_result, attempts = parse_hint_with_fallback(
                                parts[1],
                                line_stripped,
                            )

                            if attempts > 0:
                                requires_override = True

                            if parts[0].startswith("type"):
                                # hint is for argument
                                argument_name = parts[0].replace("type ", "")

                                if argument_name in argument_names:
                                    arguments[
                                        argument_names.index(argument_name)
                                    ].hint = hint_result
                            elif parts[0].startswith("rtype"):
                                # hint is for return type
                                return_type = hint_result

                comment = "\n".join(
                    filter(bool, [x.strip() for x in comment_lines])
                )

                break

    function_definition = FunctionDef(
        function_name, arguments, return_type, comment
    )

    return (function_definition, requires_override)


def store_class_override(
    file: Path, class_name: str, function_definition: FunctionDef
) -> None:
    data: Dict[str, Dict[str, Any]] = {"classes": {}, "functions": {}}

    if file.is_file():
        with open(file, "r") as r:
            data = yaml.safe_load(r)

    classes_override: Dict[str, Any] = data["classes"]

    if not class_name in classes_override:
        class_override: Dict[str, Union[List[str], Dict[str, List[str]]]] = {
            "attributes": [],
            "functions": {},
        }
    else:
        class_override = classes_override[class_name]

    if not function_definition.name in class_override["functions"]:
        function_override: List[str] = []

        class_override["functions"][
            function_definition.name
        ] = function_override

    function_override: List[str] = class_override["functions"].setdefault(
        function_definition.name, []
    )

    for argument in function_definition.arguments:
        hint_string = ""

        if argument.hint:
            hint_string = argument.hint.render()

            if argument.has_default:
                hint_string += " = ..."
        else:
            hint_string = "None"

        function_override.append(f"{argument.name}: {hint_string}")

    return_type_string = "None"

    if function_definition.return_type:
        return_type_string = function_definition.return_type.render()

    function_override.append(f"->: {return_type_string}")

    with open(file, "w") as w:
        yaml.dump(data, w, width=1000)  # type: ignore


def load_class_overrides(
    file: Path, class_name: str
) -> List[Union[ArgumentDef, FunctionDef]]:
    result: List[Union[ArgumentDef, FunctionDef]] = []

    if file.is_file():
        with open(file, "r") as r:
            data = yaml.safe_load(r)

            classes_override: Dict[str, Dict[str, Dict[str, str]]] = data[
                "classes"
            ]

            if class_name in classes_override:
                class_override = classes_override[class_name]

                for attribute in class_override["attributes"]:
                    attribute_name, attribute_definition = attribute.split(
                        ": "
                    )[:2]

                    result.append(
                        parse_override(attribute_name, attribute_definition)
                    )

                for function_name, function_arguments in class_overrides[
                    "functions"
                ].items():
                    result.append(
                        parse_override(function_name, function_arguments)
                    )

                # for member_name, member_definition in classes_override[
                #     class_name
                # ].items():
                #     result.append(
                #         parse_override(member_name, member_definition)
                #     )

    return result


def parse_class(overrides_file: Path, node: ast.ClassDef) -> ClassDef:
    class_name = node.name

    bases: List[str] = []
    attributes: List[ArgumentDef] = []

    for expression in node.bases:
        if isinstance(expression, ast.Name):
            bases.append(expression.id)

    # get all class functions
    functions: List[FunctionDef] = []

    # load overrides
    overrides = load_class_overrides(overrides_file, class_name)

    for override in overrides:
        if isinstance(override, ArgumentDef):
            attribute_override: ArgumentDef = override

            attributes.append(attribute_override)
        else:
            function_override: FunctionDef = override

            functions.append(function_override)

    for body_node in node.body:
        if isinstance(body_node, ast.FunctionDef):
            function_name = body_node.name

            if function_name not in [x.name for x in functions]:
                # function was not found in overrides
                (
                    function_definition,
                    function_requires_override,
                ) = parse_function(body_node)

                functions.append(function_definition)

                if function_requires_override:
                    store_class_override(
                        overrides_file, class_name, function_definition
                    )

    class_definition = ClassDef(class_name, bases, functions, attributes)

    return class_definition


def parse_file(
    overrides_file: Path,
    file: Path,
) -> Dict[str, Any]:
    constants: List[ConstantDef] = []

    classes: List[ClassDef] = []

    functions: List[FunctionDef] = []

    with open(file, "r") as src:
        tree = ast.parse(src.read())

        for node in tree.body:
            class_names = [x.name for x in classes]
            # function_names = [x.name for x in functions]

            if isinstance(node, ast.AnnAssign):
                if isinstance(node.target, ast.Name):
                    constants.append(ConstantDef(node.target.id))
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        constants.append(ConstantDef(target.id))
            elif isinstance(node, ast.ClassDef):
                class_definition = parse_class(overrides_file, node)

                if class_definition.name not in class_names:
                    classes.append(class_definition)
            # elif isinstance(node, ast.FunctionDef):
            #     try:
            #         function_definition = prepare_function(node)

            #         if function_definition.name not in function_names:
            #             functions.append(function_definition)
            #     except Exception:
            #         pass

    return {"constants": constants, "classes": classes, "functions": functions}


if __name__ == "__main__":
    repository_path = Path("/Users/bernhardesperester/git/cgbits/c4dstubs")

    src_directory = repository_path.joinpath("src")

    package_directory = src_directory.joinpath("c4d")

    destination_directory = repository_path.joinpath("dist")

    file = package_directory.joinpath("__init__.pyi")

    overrides_file = repository_path.joinpath("overrides.yaml")

    parse_file(overrides_file, file)

    # for root, _, filenames in os.walk(package_directory):
    #     root_path = Path(root)

    #     for filename in filenames:
    #         file = root_path.joinpath(filename)

    #         parse_file(overrides_file, file)

    # destination = destination_directory.joinpath(
    #     file.relative_to(src_directory)
    # )

    # if not destination.parent.is_dir():
    #     os.makedirs(destination.parent, mode=0o777, exist_ok=True)

    # module_path = module_path_from_file(
    #     file.relative_to(src_directory)
    # )

    # modules[module_path] = {
    #     "destination": destination,
    #     "stubs": parse_stubs(file),
    # }
