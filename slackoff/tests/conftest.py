"""Unit tests configuration file."""

import datafiles
import log


def pytest_configure(config):
    """Disable verbose output when running tests."""
    log.init(debug=True)

    terminal = config.pluginmanager.getplugin("terminal")
    terminal.TerminalReporter.showfspath = False


def pytest_runtest_setup(item):  # pylint: disable=unused-argument
    """Disable file storage during unit tests."""
    datafiles.settings.HOOKS_ENABLED = False
