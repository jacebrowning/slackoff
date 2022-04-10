# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

from slackoff import browser


def describe_detect():
    def it_returns_browser_name(expect):
        expect(browser.detect()) != ""

    def it_defaults_to_google_chrome(expect):
        expect(browser.detect({})) == "Google Chrome"


def describe_close():
    def it_handles_unknown_browsers(expect):
        expect(browser.close("Foobar")) == False
