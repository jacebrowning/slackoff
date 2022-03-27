import sys

import click
import log

from . import utils


@click.command()
@click.argument("name")
@click.option("--toggle/--no-toggle", default=True)
@click.option("--activate/--no-activate", default=True, hidden=True)
def main(name: str = "", activate: bool = True, toggle: bool = True):
    log.init()

    if activate and not utils.activate():
        click.echo("Unable to automate Slack")
        sys.exit(1)

    if utils.signout_workspace(name):
        click.echo(f"Signed out of {name}")
        sys.exit(0)

    click.echo(f"Already signed out of {name}")
    if toggle:
        utils.signin_workspace(name)


if __name__ == "__main__":  # pragma: no cover
    main()
