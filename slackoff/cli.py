import sys

import click
import log

from . import __version__, slack
from .config import settings


@click.command(help="Automatically sign out/in of a Slack workspace.")
@click.argument("workspace", nargs=-1)
@click.option(
    "--toggle/--no-toggle",
    default=True,
    help="Sign in if already signed out.",
)
@click.option("--activate/--no-activate", default=True, hidden=True)
@click.option("--debug/--no-debug", default=False, help="Show verbose logging output.")
@click.version_option(__version__)
def main(workspace: str, activate: bool, toggle: bool, debug: bool):
    log.init(debug=debug, format="%(levelname)s: %(message)s")

    if activate and not slack.activate():
        click.echo("Unable to automate Slack")
        sys.exit(1)

    workspace = get_workspace(workspace)

    if slack.signout(workspace):
        click.echo(f"Signed out of {workspace}")
        sys.exit(0)

    click.echo(f"Already signed out of {workspace}")
    if toggle:
        slack.signin(workspace)


def get_workspace(workspace):
    workspace = " ".join(workspace)
    if not workspace:
        if settings.workspaces:
            workspace = settings.workspaces[0]
        else:
            workspace = click.prompt("Slack workspace")
            settings.workspaces = [workspace]
    return workspace


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
