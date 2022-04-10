from pathlib import Path

import applescript
import log


def call(
    path: Path,
    signature: str,
    replacements: dict | None = None,
    *,
    show_error: bool = True,
) -> bool:
    functions = path.read_text("utf-8")

    if replacements is None:
        replacements = {}
    for old, new in replacements.items():
        if old != new:
            functions = functions.replace(old, new)
            log.debug(f"Replaced {old!r} => {new!r}")

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
