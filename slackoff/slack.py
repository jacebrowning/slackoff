from pathlib import Path

from . import script

FUNCTIONS = Path(__file__).parent / "slack.applescript"


def activate() -> bool:
    return script.call(FUNCTIONS, "activate()")


def signin(workspace: str) -> bool:
    return script.call(FUNCTIONS, f'signin("{workspace}")')


def signout(workspace: str) -> bool:
    return script.call(FUNCTIONS, f'signout("{workspace}")', show_error=False)
