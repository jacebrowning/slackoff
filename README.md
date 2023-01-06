# Overview

Slackoff is a quick way to sign out of a company Slack workspace at the end of the day to improve one's work-life balance. It can also be used to sign out of "fun" Slack workspaces to avoid distractions during normal working hours.

[![Build Status](https://img.shields.io/github/actions/workflow/status/jacebrowning/slackoff/main.yml?branch=main)](https://github.com/jacebrowning/slackoff/actions)
[![Coverage Status](https://img.shields.io/codecov/c/gh/jacebrowning/slackoff)](https://codecov.io/gh/jacebrowning/slackoff)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/jacebrowning/slackoff.svg)](https://scrutinizer-ci.com/g/jacebrowning/slackoff)
[![PyPI License](https://img.shields.io/pypi/l/slackoff.svg)](https://pypi.org/project/slackoff)
[![PyPI Version](https://img.shields.io/pypi/v/slackoff.svg)](https://pypi.org/project/slackoff)
[![PyPI Downloads](https://img.shields.io/pypi/dm/slackoff.svg?color=orange)](https://pypistats.org/packages/slackoff)

## Setup

### Requirements

* macOS (for AppleScript)
* Slack for Mac
* Python 3.10+

### Installation

Install this tool globally with [pipx](https://pipxproject.github.io/pipx/) (or pip):

```sh
$ pipx install slackoff
```
or add it to your [Poetry](https://python-poetry.org/docs/) project:

```sh
$ poetry add slackoff
```

## Usage

After installation, automatically sign out of a Slack workspace:

```sh
$ slackoff My Company Workspace
```

or sign back in:

```sh
$ slackoff
```

Slackoff will remember the last workspace used and attempt to toggle appropriately.

### Additional Options

To explicitly attempt to sign in or out, include the corresponding flag:

```sh
$ slackoff --signin
$ slackoff --signout
```

View the help for more options:

```sh
$ slackoff --help
```
