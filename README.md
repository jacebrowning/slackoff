# Overview

Automatically sign out of Slack workspaces (on macOS) to minimize distractions during or after working hours.

[![Build Status](https://img.shields.io/github/workflow/status/jacebrowning/slackoff/main)](https://github.com/jacebrowning/slackoff/actions)
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
$ slackoff My Workspace Name
```

or sign back in:

```sh
$ slackoff My Workspace Name
```
