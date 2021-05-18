import os

from typing import List, Optional
from pathlib import Path

from stubs.signatures import Class, Argument, Function, Hint
from stubs.parsers import load_functions, load_classes, parse_file


class Module:
    def __init__(
        self,
        name: str,
        constants: Optional[List[Argument]] = None,
        classes: Optional[List[Class]] = None,
        functions: Optional[List[Function]] = None,
    ) -> None:
        if constants is None:
            constants = []

        if classes is None:
            classes = []

        if functions is None:
            functions = []

        self.name = name
        self.constants = constants
        self.classes = classes
        self.functions = functions

    @property
    def module_name(self) -> str:
        return self.name.split(".")[-1]

    @property
    def module_path(self) -> str:
        return ".".join(self.name.split(".")[:-1])


def module_name_from_file_path(file: Path) -> str:
    file_relative_path = file.relative_to(src_directory)

    path, _ = os.path.splitext(file_relative_path)

    dirname, basename = os.path.split(path)

    if basename == "__init__":
        return dirname.replace("/", ".")
    else:
        return path.replace("/", ".")


if __name__ == "__main__":
    repository_directory = Path(
        "/Users/bernhardesperester/git/cgbits/c4dstubs"
    )

    src_directory = Path(
        "/Applications/Maxon Cinema 4D R23/resource/modules/python/libs/python37"
    )

    package_directory = src_directory.joinpath("c4d")

    destination_directory = repository_directory.joinpath("dist")

    # load overrides
    classes_file = repository_directory.joinpath("classes.yaml")

    functions_file = repository_directory.joinpath("functions.yaml")

    class_overrides: List[Class] = load_classes(classes_file)

    function_overrides: List[Function] = load_functions(functions_file)

    # gather files
    files: List[Path] = []

    for root, _, filenames in os.walk(package_directory):
        root_path = Path(root)

        for filename in filenames:
            file = root_path.joinpath(filename)

            files.append(file)

    # load modules
    modules: List[Module] = []

    for file in files:
        module_name = module_name_from_file_path(file)

        constant_instances: List[Argument] = []

        class_instances: List[Class] = []

        function_instances: List[Function] = []

        parse_file(
            file,
            constant_instances,
            class_instances,
            function_instances,
            class_overrides,
            function_overrides,
            True,
        )

        module_instance = Module(
            module_name,
            constant_instances,
            class_instances,
            function_instances,
        )

        modules.append(module_instance)
