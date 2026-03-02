# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

from slackoff.config import Workspace, settings


def describe_activate():
    def it_updates_workspaces(expect):
        settings.activate("Foobar")
        workspace = Workspace("Foobar", "", True, 1)
        expect(settings.workspaces).contains(workspace)


def describe_deactivate():
    def it_updates_workspaces(expect):
        settings.deactivate("Foobar")
        workspace = Workspace("Foobar", "", False, expect.anything)
        expect(settings.workspaces).contains(workspace)
