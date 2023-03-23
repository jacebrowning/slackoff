# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

import pytest
from click.testing import CliRunner
from expecter import expect

from slackoff.cli import main


@pytest.fixture
def runner():
    return CliRunner()


def describe_cli():
    def describe_signout():
        def it_can_force_signin(runner):
            result = runner.invoke(main, ["Foobar", "--signout"])

            expect(result.output) == "Currently signed out of Foobar\n"
            expect(result.exit_code) == 0
