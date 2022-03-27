import sys

import click
import log

from . import __version__, slack


@click.command(help="Automatically sign out/in of a Slack workspace.")
@click.argument("workspace", nargs=-1)
@click.version_option(__version__)
@click.option(
    "--toggle/--no-toggle",
    default=True,
    help="Sign in if already signed out.",
)
@click.option("--activate/--no-activate", default=True, hidden=True)
def main(workspace: str, activate: bool, toggle: bool):
    log.init()

    workspace = " ".join(workspace)

    if activate and not slack.activate():
        click.echo("Unable to automate Slack")
        sys.exit(1)

    if slack.signout(workspace):
        click.echo(f"Signed out of {workspace}")
        sys.exit(0)

    click.echo(f"Already signed out of {workspace}")
    if toggle:
        slack.signin(workspace)


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
