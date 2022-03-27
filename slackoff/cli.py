import click
import log

from . import utils


@click.command()
@click.argument("name")
@click.option("--toggle/--no-toggle", default=True)
def main(name: str = "", toggle: bool = False):
    log.init()

    if utils.signout_workspace(name):
        click.echo(f"Signed out of {name}")
    else:
        click.echo(f"Already signed out of {name}")
        if toggle:
            utils.signin_workspace(name)


if __name__ == "__main__":  # pragma: no cover
    main()
