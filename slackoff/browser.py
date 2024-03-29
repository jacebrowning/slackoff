import plistlib
from pathlib import Path

import log

from . import script

FUNCTIONS = Path(__file__).parent / "browser.applescript"
PREFERENCES = (
    Path.home()
    / "Library"
    / "Preferences"
    / "com.apple.LaunchServices/com.apple.launchservices.secure.plist"
)

NAMES = {
    "com.apple.safari": "Safari",
    "com.google.chrome": "Google Chrome",
    "org.mozilla.firefox": "Firefox",
}
DEFAULT = NAMES["com.google.chrome"]


def detect(data: dict | None = None) -> str:
    if data is None:
        if PREFERENCES.exists():
            with PREFERENCES.open("rb") as fp:
                data = plistlib.load(fp)
        else:
            log.debug(f"File not found: {PREFERENCES}")
            data = {}

    for handler in data.get("LSHandlers", []):
        if handler.get("LSHandlerURLScheme") == "http":
            role = handler["LSHandlerRoleAll"]
            name = NAMES[role]
            log.info(f"Detected default browser: {name}")
            return name

    log.warn("Unable to determine the default browser")
    return DEFAULT


def close(name: str = "") -> bool:
    replacements = {DEFAULT: name or detect()}
    return script.call(FUNCTIONS, "close()", replacements)
