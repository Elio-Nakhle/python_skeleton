import click.testing

from python_skeleton.project_name import console


class TestConsole:
    runner = click.testing.CliRunner()

    def test_main_succeeds(self):
        result = self.runner.invoke(console.main)
        assert result.exit_code == 0
