from pathlib import Path

from . import script

FUNCTIONS = Path(__file__).parent / "slack.applescript"


def activate() -> bool:
    return script.call(FUNCTIONS, "activate()")


def ready(workspace: str) -> bool:
    return script.call(FUNCTIONS, f'ready("{workspace}")', show_error=False)


def signin(workspace: str) -> bool:
    return script.call(FUNCTIONS, f'signin("{workspace}")')


def signout(workspace: str) -> bool:
    return script.call(FUNCTIONS, f'signout("{workspace}")', show_error=False)


def mute(workspace: str, channel: str) -> bool:
    return script.call(FUNCTIONS, f'mute("{workspace}", "{channel}")')


def unmute(workspace: str, channel: str) -> bool:
    return script.call(FUNCTIONS, f'unmute("{workspace}", "{channel}")')
