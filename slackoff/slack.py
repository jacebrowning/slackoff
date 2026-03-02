from pathlib import Path

from . import script

FUNCTIONS = Path(__file__).parent / "slack.applescript"
CHROME_PROFILES = Path.home() / "Library/Application Support/Google/Chrome"


def activate() -> bool:
    return script.call(FUNCTIONS, "activate()")


def ready(workspace: str) -> bool:
    return script.call(FUNCTIONS, f'ready("{workspace}")', show_error=False)


def signin(workspace: str, *, profile: str | None = None) -> bool:
    profile = profile or ""
    if profile and not (CHROME_PROFILES / profile).is_dir():
        raise ValueError(
            f"Profile {profile!r} not found. "
            "Use the profile directory name (e.g. 'Default', 'Profile 1'). "
            f"Check: {CHROME_PROFILES}"
        )
    return script.call(FUNCTIONS, f'signin("{workspace}", "{profile}")')


def signout(workspace: str) -> bool:
    return script.call(FUNCTIONS, f'signout("{workspace}")', show_error=False)


def mute(workspace: str, channel: str) -> bool:
    return script.call(FUNCTIONS, f'mute("{workspace}", "{channel}")')


def unmute(workspace: str, channel: str) -> bool:
    return script.call(FUNCTIONS, f'unmute("{workspace}", "{channel}")')
