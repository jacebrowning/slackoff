# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

from slackoff.config import Workspace, settings


def describe_activate():
    def it_updates_workspaces(expect):
        settings.activate("Foobar")
        expect(settings.workspaces).contains(Workspace("Foobar", True))


def describe_deactivate():
    def it_updates_workspaces(expect):
        settings.deactivate("Foobar")
        expect(settings.workspaces).contains(Workspace("Foobar", False))
