import click

from pathlib import Path
from c4dstubs.generator import convert_source


@click.command(
    help="Convert MAXON's Cinema 4D Dummy Package to python 3.5 type hint syntax. Make sure to omit the 'c4d' part in the end of the source directory."
)
@click.argument("source")
@click.argument("destination")
@click.argument("classes")
@click.argument("functions")
@click.option(
    "--silent/--interactive",
    default=True,
    help="Use this flag to enable asking for user input in cases where the type can not be derived",
)
def main(
    source: str,
    destination: str,
    classes: str,
    functions: str,
    silent: bool = True,
) -> None:

    source_directory = Path(source)
    destination_directory = Path(destination)

    classes_file = Path(classes)
    functions_file = Path(functions)

    if not source_directory.is_dir():
        raise ValueError(
            f"Path must be a valid directory not '{source_directory}'"
        )

    if not destination_directory.is_dir():
        raise ValueError(
            f"Path must be a valid directory not '{destination_directory}'"
        )

    if not classes_file.parent.is_dir():
        raise ValueError(
            f"Path must be a valid directory not '{classes_file.parent}'"
        )

    if not functions_file.parent.is_dir():
        raise ValueError(
            f"Path must be a valid directory not '{functions_file.parent}'"
        )

    convert_source(
        source_directory,
        destination_directory,
        classes_file,
        functions_file,
        silent,
    )


if __name__ == "__main__":
    main()
