# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

from slackoff import slack


def describe_signout():
    def it_indicates_success(expect):
        expect(slack.signout("Foobar")) == False
