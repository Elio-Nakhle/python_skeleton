"""Nox sessions."""

import os
import pathlib

import nox

repository_root_directory = pathlib.Path(__file__).parent.resolve()
locations = "python_skeleton", "tests", "docs/conf.py"
python_versions = ["3.10"]


# Needed to use pdm with nox sessions
os.environ.update({"PDM_IGNORE_SAVED_PYTHON": "1"})


@nox.session(python=python_versions[-1])
def black(session):
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=python_versions[-1])
def isort(session):
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("isort")
    session.run("isort", *args)


@nox.session(python=python_versions[-1])
def format_docstrings(session):
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("docformatter[tomli]")
    session.run("docformatter", "--recursive", "--in-place", *args)


@nox.session(python=python_versions[-1])
def eradicate(session):
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("eradicate")
    session.run("eradicate", "--recursive", "--in-place", *args)


@nox.session(python=python_versions)
def check_type_hint_annotations(session):
    """Type-check using mypy."""
    session.install("mypy")
    session.run("mypy", "-p", "python_skeleton")


@nox.session(python=python_versions)
def lint(session):
    """Lint using flake8."""
    args = session.posargs or locations
    session.install(
        "pyproject-flake8",
        "flake8",
        "flake8-bandit",
        "flake8-annotations",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "mccabe",
        "darglint",
    )
    session.run("pflake8", *args)


@nox.session(python=python_versions)
def tests(session):
    """Runs the unit tests for this project."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("pdm", "install", external=True)
    session.install("coverage[toml]", "pytest", "pytest-cov", "pytest-mock")
    session.run("pytest", *args)


@nox.session(python=python_versions)
def coverage(session):
    """Upload coverage data."""
    session.install("coverage[toml]")
    session.run("coverage", "report")
    session.run("coverage", "xml")


@nox.session(python=python_versions)
def coverage_badge(session, coverage_badge_file_name=".coverage.svg"):
    """Generate a .svg coverage badge from the coverage reports."""
    session.install("coverage[toml]", "coverage-badge")
    coverage_badge_path = str(repository_root_directory / coverage_badge_file_name)
    if os.path.exists(coverage_badge_path):
        os.remove(coverage_badge_path)
    session.run("coverage-badge", "-o", coverage_badge_file_name)


@nox.session(python=python_versions)
def docs(session):
    """Build the documentation."""
    session.run_always("pdm", "install", external=True)
    session.run("sphinx-build", "docs", "docs/_build")
