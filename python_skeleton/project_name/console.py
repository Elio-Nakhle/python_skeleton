import click
from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """This is a template project"""
    click.echo("Hello Template Project!")
