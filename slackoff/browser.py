from pathlib import Path

from . import script

FUNCTIONS = Path(__file__).parent / "browser.applescript"


def close() -> bool:
    return script.call(FUNCTIONS, "close()")
