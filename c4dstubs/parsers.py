from __future__ import annotations

import ast
import re

from pathlib import Path
from typing import Dict, Tuple, Optional, List
from c4dstubs.signatures import Class, Function, Argument, Hint
from c4dstubs.overrides import deserialize_hint


def parse_hint(hint: str) -> Hint:
    hint = hint.strip()

    if not hint:
        raise Exception("Hint must not be empty")

    if hint.startswith("function"):
        return Hint("Callable[..., Any]")

    if "maxon" in hint:
        raise Exception(f"Unknown hint '{hint}'")

    # substitute known mixups
    substitute = {
        "*": "",
        "`": "",
        "(": "[",
        ")": "]",
        ">": "",
        "<": "",
        "Slice": "List",
        "any": "Any",
        "tuple": "Tuple",
        "list": "List",
        "dict": "Dict",
        "object": "Object",
        "long": "int",
        "16float": "float",
        "optional": "Optional",
        "PyCObject": "Any",
        "string": "str",
        "false": "bool",
        "true": "bool",
        "False": "bool",
        "True": "bool",
        "number": "float",
        "intcl": "int",
        "Type": "Any",
        "buffer": "Any",
        "ptr": "Any",
        "Uuid": "UUID",
        "uuid": "UUID",
    }

    for key, value in substitute.items():
        hint = hint.replace(key, value)

    # replace
    replace = {"Object": "object"}

    for key, value in replace.items():
        if hint == key:
            hint = value

    # fix known class name typing errors
    # class_names = ["BaseObject", "LayerObject", "SplineObject", "LineObject"]

    # for class_name in class_names:
    #     pattern = re.compile(re.escape(class_name), re.IGNORECASE)
    #     hint = pattern.sub(class_name, hint)

    if " " in hint and not "[" in hint:
        raise Exception(
            f"Illeagal whitespace in hint without brackets '{hint}'"
        )

    hint_result = deserialize_hint(hint)

    for hint_instance in hint_result.get_hints():
        if hint_instance.name == "Dict":
            if len(hint_instance.children) != 2:
                hint_instance.children = [Hint("str"), Hint("Any")]
        elif hint_instance.name == "List":
            if len(hint_instance.children) != 1:
                hint_instance.children = [Hint("Any")]

    if hint_result.children and not hint_result.name:
        hint_result.name = "Union"

    return hint_result


def parse_hint_with_user_input_fallback(
    definition: str, comment: Optional[str] = None, fail_silently: bool = False
) -> Tuple[Hint, int]:
    hint: Optional[Hint] = None
    attempts: int = 0

    while hint is None:
        try:
            hint = parse_hint(definition)
        except Exception as e:
            if fail_silently:
                raise Exception(e) from e
            else:
                print(e)

                if comment:
                    print(comment)

                definition = input("Override with: ")

                attempts += 1

    return (hint, attempts)


def parse_function(
    node: ast.FunctionDef,
    function_overrides: Optional[List[Function]] = None,
    fail_silently: bool = False,
) -> Function:
    if function_overrides is None:
        function_overrides = []

    function_override_names = [x.name for x in function_overrides]
    user_input_required = False

    name = node.name
    arguments = [Argument(x.arg, Hint("Any")) for x in node.args.args]
    argument_names = [x.name for x in arguments]
    return_hint = Hint("None")
    docstring = None

    # set docstring
    for body_node in node.body:
        if isinstance(body_node, ast.Expr):
            if isinstance(body_node.value, ast.Str):
                docstring = ""

                for docstring_line in body_node.value.s.split("\n"):
                    docstring += (
                        docstring_line.strip().replace("\\", "/") + "\n"
                    )

    if name in function_override_names:
        # name is present in list of function overrides
        override_instance = function_overrides[
            function_override_names.index(name)
        ]

        # override arguments with arguments from function override
        arguments = override_instance.arguments

        # override return hint with return hint from function override
        return_hint = override_instance.return_hint
    elif docstring:
        # no override for this function was found
        # try and get more information about arguments
        # and return hint from docstring
        for docstring_line in docstring.split("\n"):
            comment = f"{name}: {docstring_line}"
            hint_parts = list(
                filter(bool, [x.strip() for x in docstring_line.split(":")])
            )

            if len(hint_parts) == 2:
                if hint_parts[0].startswith("type"):
                    # found an argument hint
                    argument_name = hint_parts[0].replace("type ", "")

                    if argument_name in argument_names:
                        argument_instance = arguments[
                            argument_names.index(argument_name)
                        ]

                        try:
                            (
                                hint_result,
                                attempts,
                            ) = parse_hint_with_user_input_fallback(
                                hint_parts[1], comment, fail_silently
                            )

                            argument_instance.hint = hint_result

                            if attempts > 0:
                                user_input_required = True
                        except Exception:
                            pass
                elif hint_parts[0].startswith("rtype"):
                    # found a return hint
                    try:
                        (
                            hint_result,
                            attempts,
                        ) = parse_hint_with_user_input_fallback(
                            hint_parts[1], comment, fail_silently
                        )

                        return_hint = hint_result

                        if attempts > 0:
                            user_input_required = True
                    except Exception:
                        pass
                elif hint_parts[0].startswith("param"):
                    # found a parameter description
                    argument_name = hint_parts[0].replace("param ", "")

                    if argument_name in argument_names:
                        argument_instance = arguments[
                            argument_names.index(argument_name)
                        ]

                        if "optional" in hint_parts[1].lower():
                            if argument_instance.hint.name != "Optional":
                                # wrap hint in Optional
                                argument_instance.hint = Hint(
                                    "Optional", [argument_instance.hint]
                                )

                            argument_instance.default = True

    function_instance = Function(name, arguments, return_hint, docstring)

    if user_input_required:
        # while defining the function user input was necessary
        # so we append the functions to the overrides list
        function_overrides.append(function_instance)

    return function_instance


def parse_class(
    node: ast.ClassDef,
    class_overrides: Optional[List[Class]] = None,
    fail_silently: bool = False,
) -> Class:
    if class_overrides is None:
        class_overrides = []

    class_names = [x.name for x in class_overrides]

    class_override: Optional[Class] = None

    name = node.name
    bases: List[str] = []
    attributes: List[Argument] = []
    functions: List[Function] = []

    attribute_overrides: List[Argument] = []
    function_overrides: List[Function] = []

    # get bases
    for expression in node.bases:
        if isinstance(expression, ast.Name):
            bases.append(expression.id)

    if name in class_names:
        # use overrides from class override
        # if name in list of class names
        class_override = class_overrides[class_names.index(name)]

        attributes = [*class_override.attributes]

        attribute_overrides = class_override.attributes
        function_overrides = class_override.functions

    for body_node in node.body:
        # parse functions from class body
        if isinstance(body_node, ast.FunctionDef):
            function_instance = parse_function(
                body_node, function_overrides, fail_silently
            )

            functions.append(function_instance)

    # add functions that have been only defined in the classs override file
    function_names: List[str] = [x.name for x in functions]

    for function_instance in function_overrides:
        if function_instance.name not in function_names:
            functions.append(function_instance)

    class_instance = Class(name, bases, attributes, functions)

    if not class_override:
        if attribute_overrides or function_overrides:
            # append class with attribute and function overrides
            class_overrides.append(
                Class(name, bases, attribute_overrides, function_overrides)
            )

    return class_instance


def parse_file(
    file: Path,
    constants: Optional[List[Argument]] = None,
    classes: Optional[List[Class]] = None,
    functions: Optional[List[Function]] = None,
    class_overrides: Optional[List[Class]] = None,
    function_overrides: Optional[List[Function]] = None,
    fail_silently: bool = False,
) -> None:
    if constants is None:
        constants = []

    if classes is None:
        classes = []

    if functions is None:
        functions = []

    if class_overrides is None:
        class_overrides = []

    if function_overrides is None:
        function_overrides = []

    with open(file, "r") as f:
        data = ast.parse(f.read())

        for node in data.body:
            if isinstance(node, ast.AnnAssign):
                if isinstance(node.target, ast.Name):
                    constants.append(
                        Argument(node.target.id, Hint("int"), True)
                    )
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        constants.append(
                            Argument(target.id, Hint("int"), True)
                        )
            elif isinstance(node, ast.ClassDef):
                class_instance = parse_class(
                    node, class_overrides, fail_silently
                )

                if class_instance.name not in [x.name for x in classes]:
                    classes.append(class_instance)
            elif isinstance(node, ast.FunctionDef):
                function_instace = parse_function(
                    node, function_overrides, fail_silently
                )

                functions.append(function_instace)


if __name__ == "__main__":
    # file = Path(
    #     "/Applications/Maxon Cinema 4D R23/resource/modules/python/libs/python37/c4d/__init__.py"
    # )

    # classes_file = Path(
    #     "/Users/bernhardesperester/git/cgbits/c4dstubs/classes.yaml"
    # )

    # functions_file = Path(
    #     "/Users/bernhardesperester/git/cgbits/c4dstubs/functions.yaml"
    # )

    # constant_instances: List[Argument] = []

    # class_instances: List[Class] = []

    # function_instances: List[Function] = []

    # classe_overrides: List[Class] = load_classes(classes_file)

    # function_overrides: List[Function] = load_functions(functions_file)

    # parse_file(
    #     file,
    #     constant_instances,
    #     class_instances,
    #     function_instances,
    #     classe_overrides,
    #     function_overrides,
    # )

    # store_classes(classes_file, classe_overrides)

    # store_functions(functions_file, function_overrides)

    # for class_instance in class_instances:
    #     print(class_instance.render())

    # for function_instance in function_instances:
    #     print(function_instance.render())

    print(parse_hint("c4d.BaseObject").signature)
