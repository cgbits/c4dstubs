import os

from math import ceil, floor
from typing import Generator, List, Optional, Dict
from pathlib import Path

from c4dstubs.signatures import Class, Argument, Function, Hint
from c4dstubs.parsers import parse_file
from c4dstubs.overrides import (
    load_functions,
    load_classes,
    store_functions,
    store_classes,
)


class Import:
    def __init__(self, name: str, module: str) -> None:
        self.name = name
        self.module = module


class Module:
    def __init__(
        self,
        name: str,
        imports: Optional[List[Import]] = None,
        constants: Optional[List[Argument]] = None,
        classes: Optional[List[Class]] = None,
        functions: Optional[List[Function]] = None,
        is_init_file: bool = False,
    ) -> None:
        if imports is None:
            imports = []

        if constants is None:
            constants = []

        if classes is None:
            classes = []

        if functions is None:
            functions = []

        self.name = name
        self.imports = imports
        self.constants = constants
        self.classes = classes
        self.functions = functions
        self.is_init_file = is_init_file

    @property
    def module_name(self) -> str:
        return self.name.split(".")[-1]

    @property
    def module_path(self) -> str:
        return ".".join(self.name.split(".")[:-1])

    @property
    def file_path(self) -> Path:
        result = self.name.replace(".", "/")

        if self.is_init_file:
            result += "/__init__"

        result += ".pyi"

        return Path(result)

    def get_hints(self) -> Generator[Hint, None, None]:
        for constant_instance in self.constants:
            yield from constant_instance.get_hints()

        for class_instance in self.classes:
            yield from class_instance.get_hints()

        for function_instance in self.functions:
            yield from function_instance.get_hints()

    def render(self) -> str:
        result = ""

        # render imports
        if self.imports:
            grouped_imports: Dict[str, List[str]] = {}

            for import_instance in self.imports:
                if import_instance.module not in grouped_imports:
                    grouped_imports[import_instance.module] = []

                grouped_imports[import_instance.module].append(
                    import_instance.name
                )

            for key, value in grouped_imports.items():
                result += f"from {key} import " + ", ".join(value) + "\n"

            result += "\n"

        # render constants
        if self.constants:
            result += "\n"

            for constant_instance in self.constants:
                result += constant_instance.render() + "\n"

            result += "\n"

        # render classes
        if self.classes:
            result += "\n"

            for class_instance in self.classes:
                result += class_instance.render()

                result += "\n"

        # render functions
        if self.functions:
            result += "\n"

            for function_instance in self.functions:
                result += function_instance.render()

                result += "\n"

        return result


def module_name_from_file_path(file: Path, src_directory: Path) -> str:
    file_relative_path = file.relative_to(src_directory)

    path, _ = os.path.splitext(file_relative_path)

    dirname, basename = os.path.split(path)

    if basename == "__init__":
        return dirname.replace("/", ".")
    else:
        return path.replace("/", ".")


def convert_source(
    src_directory: Path,
    destination_directory: Path,
    classes_file: Path,
    functions_file: Path,
    silent: bool = True,
) -> None:
    package_directory = src_directory.joinpath("c4d")

    # load overrides
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

    classes_lookup: Dict[str, str] = {"UUID": "uuid"}

    for file in files:
        module_name = module_name_from_file_path(file, src_directory)

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
            silent,
        )

        module_instance = Module(
            module_name,
            constants=constant_instances,
            classes=class_instances,
            functions=function_instances,
            is_init_file="__init__" in str(file),
        )

        for class_instance in class_instances:
            classes_lookup[class_instance.name] = module_instance.name

        modules.append(module_instance)

    # module_names = [x.module_name for x in modules]
    # module_paths = [x.module_path for x in modules]

    # update type hints
    for module_instance in modules:
        for hint_instance in module_instance.get_hints():
            if hint_instance.name:
                parts = hint_instance.name.split(".")
                class_name = parts[-1]

                if class_name in classes_lookup:
                    # class name exists in classes lookup
                    class_module_name = classes_lookup[class_name]

                    if class_module_name != module_instance.name:
                        # add class module name to list of imports
                        # if class is from different module
                        import_names = [
                            x.name for x in module_instance.imports
                        ]

                        if class_name not in import_names:
                            module_instance.imports.append(
                                Import(class_name, class_module_name)
                            )

                    # change hint to class name
                    hint_instance.name = class_name

    # update imports
    for module_instance in modules:
        if module_instance.name == "c4d":
            module_instance.imports.append(Import("*", "c4d.symbols"))

        # update imports from direct submodules
        direct_submodules: List[str] = []

        for module_name in classes_lookup.values():
            if module_name.startswith(module_instance.name):
                module_name = module_name.replace(module_instance.name, "")

                submodule_parts = list(filter(bool, module_name.split(".")))

                if submodule_parts:
                    submodule_name = submodule_parts[0]

                    if submodule_name not in direct_submodules:
                        direct_submodules.append(submodule_name)

                        module_instance.imports.append(
                            Import(submodule_name, module_instance.name)
                        )

        # update imports from class bases
        for class_instance in module_instance.classes:
            for index, base in enumerate(class_instance.bases):
                parts = base.split(".")
                class_name = parts[-1]

                if class_name in classes_lookup:
                    # class name exists in classes lookup
                    class_module_name = classes_lookup[class_name]

                    if class_module_name != module_instance.name:
                        # add class module name to list of imports
                        # if class is from different module
                        import_names = [
                            x.name for x in module_instance.imports
                        ]

                        if class_name not in import_names:
                            module_instance.imports.append(
                                Import(class_name, class_module_name)
                            )

                    class_instance.bases[index] = class_name

    # save modules
    for module_instance in modules:
        name_length = len(module_instance.name)
        line_length = 78
        padding_left = int(floor(line_length * 0.5) - floor(name_length * 0.5))
        padding_right = line_length - padding_left - name_length

        print("╔" + "═" * line_length + "╗")
        print(
            "║"
            + " " * padding_left
            + module_instance.name
            + " " * padding_right
            + "║"
        )
        print("╚" + "═" * line_length + "╝")

        print(f"Constants: {len(module_instance.constants)}")
        print(f"Classes: {len(module_instance.classes)}")
        print(f"Functions: {len(module_instance.functions)}")

        destination_file = destination_directory.joinpath(
            module_instance.file_path
        )

        if not destination_file.parent.is_dir():
            os.makedirs(destination_file.parent, mode=0o777, exist_ok=True)

        with open(destination_file, "w") as f:
            header = "from __future__ import annotations\n"
            header += "from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable\n"
            header += "\n"

            f.write(header)

            f.write(module_instance.render())

    store_classes(classes_file, class_overrides)

    store_functions(functions_file, function_overrides)
