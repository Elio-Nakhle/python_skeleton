"""Test suite for the project's command line interface."""
from typer.testing import CliRunner

from python_skeleton.project_name import console


class TestConsole:
    """Test suit for the command line interface."""

    runner = CliRunner()

    def test_main_succeeds(self):
        """It exits with a status code of zero."""
        result = self.runner.invoke(console.app, ["--version"])
        assert result.exit_code == 0
