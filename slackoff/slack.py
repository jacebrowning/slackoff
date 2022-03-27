from pathlib import Path

import applescript
import log

FUNCTIONS = Path(__file__).parent / "slack.applescript"


def activate() -> bool:
    return _call("activate()")


def signin(workspace: str) -> bool:
    return _call(f'signin("{workspace}")')


def signout(workspace: str) -> bool:
    return _call(f'signout("{workspace}")', show_error=False)


def _call(signature: str, show_error: bool = True) -> bool:
    functions = FUNCTIONS.read_text("utf-8")

    log.debug(f"Calling AppleScript: {signature}")
    result = applescript.run(functions + "\n\n" + signature)

    if result.out:
        log.debug(f"AppleScript output: {result.out}")
    if result.err:
        log.debug(f"AppleScript error: {result.err}")
        if show_error:
            message = result.err.split("error:")[-1].strip()
            log.error(message)

    return result.code == 0
