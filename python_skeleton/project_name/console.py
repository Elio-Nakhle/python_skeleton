"""Defines the command line interface of the project."""
import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """Command line interface."""
    click.echo("Hello Template Project!")
    print("Hello!")
