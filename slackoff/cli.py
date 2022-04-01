import sys

import click
import log

from . import __version__, slack
from .config import settings


@click.command(help="Automatically sign out/in of a Slack workspace.")
@click.argument("workspace", nargs=-1)
@click.option(
    "-o", "--signout", is_flag=True, default=False, help="Only attempt to sign out."
)
@click.option(
    "-i", "--signin", is_flag=True, default=False, help="Only attempt to sign in."
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

    if not signin:
        if slack.signout(workspace):
            click.echo(f"Signed out of {workspace}")
            settings.deactivate(workspace)
            sys.exit(0)
        else:
            click.echo(f"Already signed out of {workspace}")

    if not signout:
        if not slack.signin(workspace):
            click.echo(f"Click 'Open' to sign in to {workspace}")
        settings.activate(workspace)


def get_workspace(workspace: str) -> str:
    workspace = " ".join(workspace)
    if not workspace:
        if settings.workspaces:
            workspace = settings.workspaces[0].name
        else:
            workspace = click.prompt("Slack workspace")
    log.debug(f"Modifying workspace: {workspace}")
    return workspace


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
