# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

from slackoff import utils


def describe_signout_workspace():
    def it_indicates_success(expect):
        expect(utils.signout_workspace("Foobar")) == False
