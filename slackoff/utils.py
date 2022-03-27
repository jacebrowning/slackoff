from pathlib import Path

import applescript

FUNCTIONS = Path(__file__).parent / "slack.applescript"


def activate() -> bool:
    functions = FUNCTIONS.read_text("utf-8")
    result = applescript.run(functions + " activate()")
    return result.code == 0


def signin_workspace(name: str) -> bool:
    functions = FUNCTIONS.read_text("utf-8")
    result = applescript.run(functions + f' signin("{name}")')
    return result.code == 0


def signout_workspace(name: str) -> bool:
    functions = FUNCTIONS.read_text("utf-8")
    result = applescript.run(functions + f' signout("{name}")')
    return result.code == 0
