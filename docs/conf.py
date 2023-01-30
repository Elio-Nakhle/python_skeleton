"""Sphinx configuration."""
project = "project-template"
author = "Elio Nakhle"
copyright = f"2022, {author}"
html_theme = "classic"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]
