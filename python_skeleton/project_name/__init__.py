"""This is a template python project."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("python_skeleton")
except PackageNotFoundError:
    __version__ = "unknown"
