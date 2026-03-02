import sys
import time
from contextlib import suppress
from pathlib import Path

import click
import log
import pync

from . import __version__, browser, slack
from .config import PATH, settings


def clean_channel(_ctx, _param, value: str | None) -> str:
    if value is None:
        return ""
    if value := value.strip("# "):
        return value
    raise click.BadParameter("Invalid channel name.")


@click.command(help="Automatically sign out of Slack workspaces.")
@click.argument("workspace", nargs=-1)
@click.option(
    "-i", "--signin", is_flag=True, default=False, help="Only attempt to sign in."
)
@click.option(
    "-p",
    "--profile",
    metavar="NAME",
    default=None,
    help="Browser profile for sign in.",
)
@click.option(
    "-o", "--signout", is_flag=True, default=False, help="Only attempt to sign out."
)
@click.option(
    "-m",
    "--mute",
    metavar="NAME",
    callback=clean_channel,
    help="Mute the specified channel.",
)
@click.option(
    "-u",
    "--unmute",
    metavar="NAME",
    callback=clean_channel,
    help="Unmute the specified channel.",
)
@click.option(
    "--edit", is_flag=True, default=False, help="Open the configuration file."
)
@click.option(
    "--debug", is_flag=True, default=False, help="Show verbose logging output."
)
@click.version_option(__version__)
@click.help_option("-h", "--help")
def main(
    workspace: str,
    signin: bool,
    profile: str | None,
    signout: bool,
    mute: str,
    unmute: str,
    edit: bool,
    debug: bool,
):
    log.init(debug=debug, format="%(levelname)s: %(message)s")

    if edit:
        path = Path(PATH).expanduser()
        click.edit(filename=str(path))
        sys.exit(0)

    explicit = bool(workspace)
    workspace = get_workspace(workspace)

    if not (signin or signout) and not slack.activate():
        sys.exit(1)

    if signin:
        try:
            code = 0 if attempt_signin(workspace, profile) else 2
        except ValueError as err:
            click.echo(err, err=True)
            sys.exit(2)
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
        try:
            attempt_signin(workspace, profile)
        except ValueError as err:
            click.echo(err, err=True)
            sys.exit(2)


def get_workspace(workspace: str) -> str:
    workspace = " ".join(workspace)

    if not workspace:
        if settings.workspaces:
            workspace = settings.workspaces[0].name
        else:
            workspace = click.prompt("Slack workspace")

    log.debug(f"Modifying workspace: {workspace}")
    return workspace


def attempt_signin(workspace: str, profile: str | None = None) -> bool:
    if profile is None:
        profile = settings.get_profile(workspace)
    if profile and browser.detect() != "Google Chrome":
        raise ValueError(
            "--profile is only supported when Chrome is the default browser"
        )
    if not slack.signin(workspace, profile=profile):
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

    settings.activate(workspace, profile)
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
            ready = attempt_signin(workspace, None)
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
            ready = attempt_signin(workspace, None)
        if not ready:
            click.echo(f"Workspace not available: {workspace}")
            return False
    elif not ready:
        workspace = "current workspace"

    click.echo(f"Unmuting #{channel} in {workspace}")
    return slack.unmute(workspace, channel)


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
