import yaml

from typing import List, Dict, Union, Any
from pathlib import Path
from stubs.signatures import Class, Function, Argument, Hint


def deserialize_hint(hint_string: str) -> Hint:
    # handle nested definitions in brackets
    opening_bracket_index = hint_string.find("[")
    closing_bracket_index = hint_string[::-1].find("]")

    if opening_bracket_index > -1 or closing_bracket_index > -1:
        # we have opening and or closing brackets
        if opening_bracket_index > -1 and closing_bracket_index > -1:
            # opening and closing brackets are present
            start = opening_bracket_index + 1
            stop = len(hint_string) - closing_bracket_index - 1

            hint_substring = hint_string[start:stop]

            hint_instance = deserialize_hint(hint_string[: start - 1])

            if "[" in hint_substring:
                hint_instance.children = [deserialize_hint(hint_substring)]
            else:
                hint_instance.children = [
                    deserialize_hint(x) for x in hint_substring.split(",")
                ]

            return hint_instance
        else:
            raise Exception(f"Missing bracket counterpart in '{hint_string}'")
    else:
        return Hint(hint_string)


def deserialize_argument(argument_string: str) -> Argument:
    default = False
    value_parts = list(
        filter(bool, [x.strip() for x in argument_string.split("=")])
    )

    if len(value_parts) > 1:
        default = True

    name_hint_parts = list(
        filter(bool, [x.strip() for x in value_parts[0].split(":")])
    )

    name = name_hint_parts[0]
    hint = Hint("None")

    if len(name_hint_parts) > 1:
        hint = deserialize_hint(name_hint_parts[1])

    return Argument(name, hint, default)


def serialize_function(function_instance: Function) -> Dict[str, List[str]]:
    return {
        function_instance.name: [
            x.signature for x in function_instance.arguments
        ]
        + [Argument("->", function_instance.return_hint).signature]
    }


def deserialize_function(
    function_name: str, argument_strings: List[str]
) -> Function:
    arguments: List[Argument] = []
    return_hint: Hint = Hint("None")

    for argument_string in argument_strings:
        argument_instance = deserialize_argument(argument_string)

        if argument_instance.name == "->":
            return_hint = argument_instance.hint
        else:
            arguments.append(argument_instance)

    return Function(function_name, arguments, return_hint)


def serialize_class(
    class_instance: Class,
) -> Dict[str, Dict[str, Union[List[str], Dict[str, List[str]]]]]:
    attributes: List[str] = [x.signature for x in class_instance.attributes]
    functions: Dict[str, List[str]] = {}

    for function_instance in class_instance.functions:
        functions = {**functions, **serialize_function(function_instance)}

    return {
        class_instance.name
        + class_instance.signature: {
            "attributes": attributes,
            "functions": functions,
        }
    }


def deserialize_class(
    class_name: str,
    attribute_strings: List[str],
    function_strings: Dict[str, List[str]],
) -> Class:
    bases: List[str] = []
    attributes: List[Argument] = []
    functions: List[Function] = []

    if "(" in class_name:
        parts = list(filter(bool, [x.strip() for x in class_name.split("(")]))

        class_name = parts[0]

        if len(parts) > 1:
            base_part = parts[1][:-1]

            bases = list(
                filter(bool, [x.strip() for x in base_part.split(",")])
            )

    # deserialize attributes
    for attribute_string in attribute_strings:
        attributes.append(deserialize_argument(attribute_string))

    # deserialize functions
    for function_name, function_argument_strings in function_strings.items():
        functions.append(
            deserialize_function(function_name, function_argument_strings)
        )

    return Class(class_name, bases, attributes, functions)


def deserialize_classes(data: Dict[str, Any]) -> List[Class]:
    result: List[Class] = []

    for class_name, class_members in data.items():
        attributes = class_members["attributes"]
        functions = class_members["functions"]

        result.append(deserialize_class(class_name, attributes, functions))

    return result


def deserialize_functions(data: Dict[str, Any]) -> List[Function]:
    result: List[Function] = []

    for function_name, function_arguments in data.items():
        result.append(deserialize_function(function_name, function_arguments))

    return result


def load_classes(
    file: Path,
) -> List[Class]:
    result: List[Class] = []

    if file.is_file():
        with open(file, "r") as f:
            data = yaml.safe_load(f)

            result = deserialize_classes(data)

    return result


def load_functions(file: Path) -> List[Function]:
    result: List[Function] = []

    if file.is_file():
        with open(file, "r") as f:
            data = yaml.safe_load(f)

            result = deserialize_functions(data)

    return result


def store_classes(file: Path, class_instances: List[Class]) -> None:
    with open(file, "w") as f:
        data: Dict[str, Any] = {}

        for class_instance in class_instances:
            data = {**data, **serialize_class(class_instance)}

        yaml.safe_dump(data, f, width=1000)  # type: ignore


def store_functions(file: Path, function_instances: List[Function]) -> None:
    with open(file, "w") as f:
        data: Dict[str, Any] = {}

        for function_instance in function_instances:
            data = {**data, **serialize_function(function_instance)}

        yaml.safe_dump(data, f, width=1000)  # type: ignore


if __name__ == "__main__":
    class_instance = Class(
        "BaseObject",
        ["BaseList2D"],
        attributes=[Argument("x", Hint("float"))],
        functions=[
            Function("GetName", [Argument("self")], Hint("str")),
            Function(
                "SetName",
                [Argument("self"), Argument("name", Hint("str"), True)],
            ),
            Function(
                "GetChildren",
                [Argument("self")],
                Hint("List", [Hint("BaseObject")]),
            ),
            Function("Foobar", return_hint=Hint("str")),
        ],
    )

    classes_file = Path(
        "/Users/bernhardesperester/git/cgbits/c4dstubs/classes.yaml"
    )

    store_classes(classes_file, [class_instance])

    class_instances = load_classes(classes_file)

    for class_instance in class_instances:
        print(class_instance.render())

    # test functions

    function_instance = Function(
        "MatrixToHPB", [Argument("m", Hint("c4d.Matrix"))], Hint("c4d.Vector")
    )

    functions_file = Path(
        "/Users/bernhardesperester/git/cgbits/c4dstubs/functions.yaml"
    )

    store_functions(functions_file, [function_instance])

    function_instances = load_functions(functions_file)

    for function_instance in function_instances:
        print(function_instance.render())
