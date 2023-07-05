"""Defines the command line interface of the project."""
import click

from python_skeleton.project_name import __version__


@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """Command line interface."""
    click.echo("Hello Template Project!")
