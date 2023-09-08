"""Defines the command line interface of the project."""
from typing import Optional

import typer
from typing_extensions import Annotated

from python_skeleton.project_name import __version__

app = typer.Typer()


def version_callback(value: bool) -> None:
    """Return package version.

    Callback for the version cli argument:

    Args:
        value (bool): Specify wether to return version or not.
    """
    if value:
        typer.echo(f"Template Project Version: {__version__}")
        typer.Exit()


@app.command()
def main(
    version: Annotated[
        Optional[bool], typer.Option("--version", callback=version_callback, is_eager=True)
    ] = False
) -> None:
    """Command line interface.

    console.py's cli entry point with option definition:

    Args:
        version: Add version option for console's cli
    """
    typer.echo("Hello Template Project!")


if __name__ == "__main__":
    app()
