import sys
import time
from contextlib import suppress

import click
import log
import pync

from . import __version__, browser, slack
from .config import settings


@click.command(help="Automatically sign out/in of a Slack workspace.")
@click.argument("workspace", nargs=-1)
@click.option(
    "-i", "--signin", is_flag=True, default=False, help="Only attempt to sign in."
)
@click.option(
    "-o", "--signout", is_flag=True, default=False, help="Only attempt to sign out."
)
@click.option(
    "--debug", is_flag=True, default=False, help="Show verbose logging output."
)
@click.version_option(__version__)
def main(workspace: str, signin: bool, signout: bool, debug: bool):
    log.init(debug=debug, format="%(levelname)s: %(message)s")

    workspace = get_workspace(workspace)

    if not (signin or signout) and not slack.activate():
        sys.exit(1)

    if signin:
        attempt_signin(workspace)
        sys.exit(0)

    if signout:
        attempt_signout(workspace)
        sys.exit(0)

    if not attempt_signout(workspace):
        click.echo(f"Signing in to {workspace}")
        attempt_signin(workspace)


def get_workspace(workspace: str) -> str:
    workspace = " ".join(workspace)

    if not workspace:
        if settings.workspaces:
            workspace = settings.workspaces[0].name
        else:
            workspace = click.prompt("Slack workspace")

    log.debug(f"Modifying workspace: {workspace}")
    return workspace


def attempt_signin(workspace) -> bool:
    if not slack.signin(workspace):
        message = f"Click 'Open' to sign in to {workspace}"

        if not slack.ready(workspace):
            pync.notify(message, title="Slackoff")
            click.echo(message + "...")

        with suppress(KeyboardInterrupt):
            while not slack.ready(workspace):
                log.debug(f"Waiting for workspace: {workspace}")
                time.sleep(1)
            click.echo(f"Signed in to of {workspace}")

        browser.close()

    settings.activate(workspace)
    return True


def attempt_signout(workspace) -> bool:
    if slack.signout(workspace):
        click.echo(f"Signed out of {workspace}")
        settings.deactivate(workspace)
        log.debug("Waiting for extra browser tabs")
        time.sleep(5)
        browser.close()
        return True

    click.echo(f"Currently signed out of {workspace}")
    return False


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
