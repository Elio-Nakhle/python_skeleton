"""Test suite for the project's command line interface."""
import click.testing

from python_skeleton.project_name import console


class TestConsole:
    """Test suit for the command line interface."""

    runner = click.testing.CliRunner()

    def test_main_succeeds(self):
        """It exits with a status code of zero."""
        result = self.runner.invoke(console.main)
        assert result.exit_code == 0
