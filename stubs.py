from __future__ import annotations

import os
import re
import ast

from typing import List, Optional, Any
from pathlib import Path


class ClassDefinition:
    def __init__(
        self,
        name: str,
        bases: Optional[List[str]] = None,
        functions: Optional[List[FunctionDefinition]] = None,
    ) -> None:
        if functions is None:
            functions = []

        if bases is None:
            bases = []

        self.name = name
        self.bases = bases
        self.functions = functions

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} {self.definition} at {hex(id(self))}>"
        )

    @property
    def definition(self) -> str:
        bases = ", ".join(self.bases)

        return f"class {self.name}({bases}):"

    def render(self) -> str:
        lines = [self.definition]

        for function in self.functions:
            lines += ["", ""]
            lines += [" " * 4 + x for x in function.render().split("\n")]

        return "\n".join(lines)


class FunctionDefinition:
    def __init__(
        self,
        name: str,
        arguments: Optional[List[Argument]] = None,
        returntype: Optional[str] = None,
    ) -> None:
        if arguments is None:
            arguments = []

        self.name = name
        self.arguments = arguments
        self.returntype = returntype

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} {self.definition} at {hex(id(self))}>"
        )

    @property
    def definition(self) -> str:
        returntype = self.returntype

        if self.name == "__init__":
            returntype = None

        arguments = ", ".join([str(x) for x in self.arguments])

        return f"def {self.name}({arguments}) -> {returntype}:"

    def render(self) -> str:
        lines: List[str] = [self.definition, " " * 4 + "..."]

        return "\n".join(lines)


class Argument:
    def __init__(
        self,
        name: str,
        type: Optional[str] = None,
        has_default: bool = False,
        default: Optional[Any] = None,
    ) -> None:
        self.name = name
        self.type = type
        self.has_default = has_default
        self.default = default

    def __repr__(self) -> str:
        base = self.name

        if self.type is not None:
            base += f": {self.type}"

        if self.has_default:
            base += f" = {self.default}"

        return base


def prepare_typehint(hint: str) -> str:
    if hint == "Object":
        hint = "object"

    hint = hint.replace("any", "Any")

    hint = hint.replace("dict", "Dict[str, Any]")

    hint = hint.replace("tuple", "Tuple")

    hint = hint.replace("(", "[").replace(")", "]")

    return hint


def create_function_stub(node: ast.FunctionDef) -> FunctionDefinition:
    # list of arguments
    function_arguments: List[Argument] = [
        Argument(x.arg) for x in node.args.args
    ]

    function_definition = FunctionDefinition(node.name, function_arguments)

    argument_names = [x.name for x in function_arguments]

    # parse comment
    for body_node in node.body:
        if isinstance(body_node, ast.Expr):
            if isinstance(body_node.value, ast.Str):
                comment = body_node.value.s

                comment_lines = comment.split("\n")

                for comment_line in comment_lines:
                    argument_match = re.search(
                        re.compile(r":type\s(\w+:\s[\w\\[\].\,\(\)\s]+)"),
                        comment_line.strip(),
                    )

                    if argument_match:
                        argument_name, argument_type = [
                            x.strip()
                            for x in argument_match.group(1).split(":")
                        ]

                        if argument_name in argument_names:
                            function_arguments[
                                argument_names.index(argument_name)
                            ].type = prepare_typehint(argument_type)

                    returntype_match = re.search(
                        re.compile(r":rtype:\s([\w\\[\].\,\s\(\)\s]+)"),
                        comment_line.strip(),
                    )

                    if returntype_match:
                        returntype = returntype_match.group(1)

                        function_definition.returntype = prepare_typehint(
                            returntype
                        )

    return function_definition


def create_class_stub(node: ast.ClassDef) -> ClassDefinition:
    bases: List[str] = []

    for expression in node.bases:
        if isinstance(expression, ast.Name):
            bases.append(expression.id)

    class_definition = ClassDefinition(node.name, bases)

    for body_node in node.body:
        if isinstance(body_node, ast.FunctionDef):
            class_definition.functions.append(create_function_stub(body_node))

    return class_definition


def create_stubs(file: Path, destination: Path) -> None:
    with open(destination, "w") as fw:
        fw.write("from __future__ import annotations\n")
        fw.write("from typing import Union, List, Tuple, Dict, Any\n")

        with open(file, "r") as fs:
            tree = ast.parse(fs.read())

            for node in tree.body:
                if isinstance(node, ast.ImportFrom):
                    modules = ", ".join([x.name for x in node.names])

                    fw.write(f"from {node.module} import {modules}\n")
                elif isinstance(node, ast.FunctionDef):
                    function_definition = create_function_stub(node)

                    fw.write("\n\n" + function_definition.render() + "\n")

                    # print(ast.dump(node))
                elif isinstance(node, ast.ClassDef):
                    class_definition = create_class_stub(node)

                    fw.write("\n\n" + class_definition.render() + "\n")
                elif isinstance(node, ast.AnnAssign):
                    if isinstance(node.target, ast.Name):
                        fw.write(f"{node.target.id}: int = ...\n")
                elif isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            fw.write(f"{target.id}: int = ...\n")
                else:
                    print(ast.dump(node))


if __name__ == "__main__":
    base_directory = Path(
        os.path.join(os.path.dirname(__file__), "typings/c4d")
    )

    destination_directory = Path(
        os.path.join(os.path.dirname(__file__), "dist/c4d")
    )

    for root, dirnames, filenames in os.walk(base_directory):
        root_path = Path(root)

        for filename in filenames:
            file = root_path.joinpath(filename)

            destination = destination_directory.joinpath(
                file.relative_to(base_directory)
            )

            if not destination.parent.is_dir():
                os.makedirs(destination.parent, mode=0o777, exist_ok=True)

            create_stubs(file, destination)
