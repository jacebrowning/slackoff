import sys
import time
from contextlib import suppress

import click
import log
import pync

from . import __version__, browser, slack
from .config import settings


def clean_channel(_ctx, _param, value: str | None) -> str:
    if value is None:
        return ""
    if value := value.strip("# "):
        return value
    raise click.BadParameter("Invalid channel name.")


@click.command(help="Automatically sign out/in of a Slack workspace.")
@click.argument("workspace", nargs=-1)
@click.option(
    "-i", "--signin", is_flag=True, default=False, help="Only attempt to sign in."
)
@click.option(
    "-o", "--signout", is_flag=True, default=False, help="Only attempt to sign out."
)
@click.option(
    "-m", "--mute", callback=clean_channel, help="Mute the specified channel."
)
@click.option(
    "-u", "--unmute", callback=clean_channel, help="Unmute the specified channel."
)
@click.option(
    "--debug", is_flag=True, default=False, help="Show verbose logging output."
)
@click.version_option(__version__)
@click.help_option("-h", "--help")
def main(
    workspace: str, signin: bool, signout: bool, mute: str, unmute: str, debug: bool
):
    log.init(debug=debug, format="%(levelname)s: %(message)s")

    explicit = bool(workspace)
    workspace = get_workspace(workspace)

    if not (signin or signout) and not slack.activate():
        sys.exit(1)

    if signin:
        code = 0 if attempt_signin(workspace) else 2
        sys.exit(code)

    if signout:
        attempt_signout(workspace)
        sys.exit(0)

    if mute:
        code = 0 if attempt_mute(workspace, explicit, mute) else 2
        sys.exit(code)

    if unmute:
        code = 0 if attempt_unmute(workspace, explicit, unmute) else 2
        sys.exit(code)

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
        time.sleep(10)
        browser.close()
        return True

    click.echo(f"Currently signed out of {workspace}")
    return False


def attempt_mute(workspace: str, explicit: bool, channel: str) -> bool:
    ready = slack.ready(workspace)
    if explicit:
        if not ready:
            ready = attempt_signin(workspace)
        if not ready:
            click.echo(f"Workspace not available: {workspace}")
            return False
    elif not ready:
        workspace = "current workspace"

    click.echo(f"Muting #{channel} in {workspace}")
    return slack.mute(workspace, channel)


def attempt_unmute(workspace: str, explicit: bool, channel: str) -> bool:
    ready = slack.ready(workspace)
    if explicit:
        if not ready:
            ready = attempt_signin(workspace)
        if not ready:
            click.echo(f"Workspace not available: {workspace}")
            return False
    elif not ready:
        workspace = "current workspace"

    click.echo(f"Unmuting #{channel} in {workspace}")
    return slack.unmute(workspace, channel)


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
