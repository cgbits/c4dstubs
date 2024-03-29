from __future__ import annotations

from typing import Optional, List, Generator


class Signature:
    @property
    def signature(self) -> str:
        return ""

    @property
    def definition(self) -> str:
        return self.signature

    def render(self) -> str:
        return self.definition


class Hint(Signature):
    def __init__(
        self, name: Optional[str] = None, children: Optional[List[Hint]] = None
    ) -> None:
        if children is None:
            children = []

        self.name = name
        self.children = children

    @property
    def signature(self) -> str:
        result = ""

        if self.name:
            result = self.name

        if self.children:
            # add children to signature
            # if children exist
            result += "["

            result += ", ".join([x.signature for x in self.children])

            result += "]"

        return result

    @property
    def definition(self) -> str:
        return self.signature

    def render(self) -> str:
        return self.definition

    def get_hints(self) -> Generator[Hint, None, None]:
        yield self

        for child in self.children:
            yield from child.get_hints()


class Argument(Signature):
    def __init__(
        self, name: str, hint: Optional[Hint] = None, default: bool = False
    ) -> None:
        if hint is None:
            hint = Hint("None")

        self.name = name
        self.hint = hint
        self.default = default

    @property
    def signature(self) -> str:
        result = self.name

        if self.name != "self":
            # add hint and default value
            # if name is not self
            result += f": {self.hint.signature}"

            if self.default or self.hint.name == "Optional":
                result += " = ..."

        return result

    @property
    def definition(self) -> str:
        return self.signature

    def render(self) -> str:
        return self.definition

    def get_hints(self) -> Generator[Hint, None, None]:
        yield from self.hint.get_hints()


class Function(Signature):
    def __init__(
        self,
        name: str,
        arguments: Optional[List[Argument]] = None,
        return_hint: Optional[Hint] = None,
        docstring: Optional[str] = None,
    ) -> None:
        if arguments is None:
            arguments = []

        if return_hint is None:
            return_hint = Hint("None")

        self.name = name
        self.arguments = arguments
        self.return_hint = return_hint
        self.docstring = docstring

    @property
    def signature(self) -> str:
        result = "("

        argument_signatures: List[str] = []

        for index, argument_signature in enumerate(self.arguments):
            if index > 0:
                # test if previous argument is optional
                if self.arguments[index - 1].hint.name == "Optional":
                    if argument_signature.hint.name != "Optional":
                        argument_signature.hint = Hint(
                            "Optional", [argument_signature.hint]
                        )

            argument_signatures.append(argument_signature.signature)

        result += ", ".join(argument_signatures)

        return_hint_signature = "None"

        if self.name != "__init__":
            return_hint_signature = self.return_hint.signature

        result += f") -> {return_hint_signature}"

        return result

    @property
    def definition(self) -> str:
        return f"def {self.name}{self.signature}"

    def render(self) -> str:
        result = f"{self.definition}:\n"

        if self.docstring:
            result += " " * 4 + '"""'

            for docstring_line in self.docstring.split("\n"):
                result += " " * 4 + docstring_line + "\n"

            result += " " * 4 + '"""'

            result += "\n"

        result += " " * 4 + "...\n"

        return result

    def get_hints(self) -> Generator[Hint, None, None]:
        yield from self.return_hint.get_hints()

        for argument in self.arguments:
            yield from argument.get_hints()


class Class(Signature):
    def __init__(
        self,
        name: str,
        bases: Optional[List[str]] = None,
        attributes: Optional[List[Argument]] = None,
        functions: Optional[List[Function]] = None,
    ) -> None:
        if bases is None:
            bases = []

        if attributes is None:
            attributes = []

        if functions is None:
            functions = []

        self.name = name
        self.bases = bases
        self.attributes = attributes
        self.functions = functions

    @property
    def signature(self) -> str:
        result = ""

        if self.bases:
            result += "("
            result += ", ".join(self.bases)
            result += ")"

        return result

    @property
    def definition(self) -> str:
        return f"class {self.name}{self.signature}"

    def render(self) -> str:
        result = f"{self.definition}:\n"

        if self.attributes or self.functions:
            if self.attributes:
                # add attributes to result
                for attribute_instance in self.attributes:
                    result += " " * 4 + attribute_instance.render() + "\n"

                result += "\n"

            for function_instance in self.functions:
                if function_instance.arguments:
                    if function_instance.arguments[0].name == "cls":
                        # function must be a class method
                        # because the first arguments name is cls
                        result += " " * 4 + "@classmethod\n"

                if (
                    not function_instance.arguments
                    or function_instance.arguments[0].name != "self"
                ):
                    # function must be a static method
                    # because the first arguments name is not self
                    # or because the function takes no arguments
                    result += " " * 4 + "@staticmethod\n"

                # append function to result
                for function_line in function_instance.render().split("\n"):
                    result += " " * 4 + function_line + "\n"
        else:
            result += " " * 4 + "...\n"

        return result

    def get_hints(self) -> Generator[Hint, None, None]:
        for attribute in self.attributes:
            yield from attribute.get_hints()

        for function in self.functions:
            yield from function.get_hints()
