"""Nox sessions."""
# import os
# import pathlib
# import shutil

import nox

locations = "python_skeleton", "tests", "noxfile.py", "docs/conf.py"
python_versions = ["3.10"]


@nox.session(python=python_versions)
def mypy(session):
    """Type-check using mypy."""
    session.install("mypy")
    session.run("mypy", "python_skeleton")


@nox.session(python=python_versions)
def lint(session):
    """Lint using flake8."""
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-bandit",
        "flake8-annotations",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "darglint",
    )
    session.run("flake8", *args)


@nox.session(python=python_versions)
def black(session):
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=python_versions)
def isort(session):
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("isort")
    session.run("isort", *args)


@nox.session(python=python_versions)
def docs(session):
    """Build the documentation."""
    session.run("poetry", "install", "--no-dev", external=True)
    session.install("sphinx", "sphinx-autodoc-typehints", "sphinx_rtd_theme")
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session(python=python_versions)
def coverage(session):
    """Upload coverage data."""
    session.install("coverage[toml]")
    session.run("coverage", "report")
    session.run("coverage", "xml")


@nox.session(python=python_versions)
def tests(session):
    """Runs the unit tests for this project."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", "--no-dev", external=True)
    session.install("coverage[toml]", "pytest", "pytest-cov", "pytest-mock")
    session.run("pytest", *args)


# TODO: find a way to exclude this from poetry run nox
# @nox.session(python=python_versions)
# def clean(session):
#     """Remove generated files."""
#     print(f"Running nox session: {session.name}")
#     root_directory = str(pathlib.Path(__file__).parent.resolve()) + "/"
#     print(f"Cleaning up specified files in: {root_directory}")
#     files_to_remove = [".coverage", "coverage.xml"]
#     files_to_remove = [root_directory + file for file in files_to_remove]
#     [os.remove(file) for file in files_to_remove if os.path.isfile(file)]
#
#     directories_to_remove = ["docs/_build", ".mypy_cache", ".nox", ".pytest_cache", ".venv"]
#     directories_to_remove = [root_directory + directory for directory in directories_to_remove]
#     [
#         shutil.rmtree(directory, ignore_errors=True)
#         for directory in directories_to_remove
#         if os.path.isdir(directory)
#     ]
