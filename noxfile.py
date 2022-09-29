"""Nox sessions."""
import nox

locations = "python_skeleton", "tests", "noxfile.py", "docs/conf.py"


@nox.session(python=["3.10"])
def mypy(session):
    """Type-check using mypy."""
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)


@nox.session(python=["3.10"])
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
        "flake8-import-order",
        "darglint",
    )
    session.run("flake8", *args)


@nox.session(python="3.10")
def black(session):
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python="3.10")
def isort(session):
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("isort")
    session.run("isort", *args)


@nox.session(python="3.10")
def docs(session):
    """Build the documentation."""
    session.run("poetry", "install", "--no-dev", external=True)
    session.install("sphinx", "sphinx-autodoc-typehints")
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session(python="3.10")
def coverage(session):
    """Upload coverage data."""
    session.install("coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)


@nox.session(python="3.10")
def tests(session):
    """Runs the unit tests for this project."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", "--no-dev", external=True)
    session.install("coverage[toml]", "pytest", "pytest-cov", "pytest-mock")
    session.run("pytest", *args)
