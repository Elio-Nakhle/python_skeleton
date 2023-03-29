"""Sphinx configuration."""
project = "project-template"
author = "Elio Nakhle"
copyright = f"2023, {author}"
html_theme = "sphinx_rtd_theme"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]
