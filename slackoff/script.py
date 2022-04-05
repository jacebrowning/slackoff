from pathlib import Path

import applescript
import log


def call(path: Path, signature: str, *, show_error: bool = True) -> bool:
    functions = path.read_text("utf-8")

    log.debug(f"Calling AppleScript: {signature}")
    result = applescript.run(functions + "\n\n" + signature)

    log.debug(f"AppleScript code: {result.code}")
    if result.out:
        log.debug(f"AppleScript output: {result.out}")
    if result.err:
        log.debug(f"AppleScript error: {result.err}")
        if show_error:
            message = result.err.split("error:")[-1].strip()
            log.error(message)

    return result.code == 0 and "missing value" not in result.out
