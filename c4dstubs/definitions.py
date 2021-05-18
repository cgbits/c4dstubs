from __future__ import annotations

import os
import ast

from typing import Any, Callable, Generator, List, Dict, Optional, Tuple, Union
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
