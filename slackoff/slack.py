from pathlib import Path

import applescript

FUNCTIONS = Path(__file__).parent / "slack.applescript"


def activate() -> bool:
    functions = FUNCTIONS.read_text("utf-8")
    result = applescript.run(functions + " activate()")
    return result.code == 0


def signin(workspace: str) -> bool:
    functions = FUNCTIONS.read_text("utf-8")
    result = applescript.run(functions + f' signin("{workspace}")')
    return result.code == 0


def signout(workspace: str) -> bool:
    functions = FUNCTIONS.read_text("utf-8")
    result = applescript.run(functions + f' signout("{workspace}")')
    return result.code == 0
