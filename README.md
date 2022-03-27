# Overview

Automatically sign out of Slack workspaces on macOS.

[![Unix Build Status](https://img.shields.io/travis/com/jacebrowning/slackoff.svg?label=unix)](https://travis-ci.com/jacebrowning/slackoff)
[![Windows Build Status](https://img.shields.io/appveyor/ci/jacebrowning/slackoff.svg?label=windows)](https://ci.appveyor.com/project/jacebrowning/slackoff)
[![Coverage Status](https://img.shields.io/codecov/c/gh/jacebrowning/slackoff)](https://codecov.io/gh/jacebrowning/slackoff)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/jacebrowning/slackoff.svg)](https://scrutinizer-ci.com/g/jacebrowning/slackoff)
[![PyPI License](https://img.shields.io/pypi/l/slackoff.svg)](https://pypi.org/project/slackoff)
[![PyPI Version](https://img.shields.io/pypi/v/slackoff.svg)](https://pypi.org/project/slackoff)
[![PyPI Downloads](https://img.shields.io/pypi/dm/slackoff.svg?color=orange)](https://pypistats.org/packages/slackoff)

# Setup

## Requirements

* macOS
* Slack for Mac
* Python 3.10+

## Installation

Install this tool globally with [pipx](https://pipxproject.github.io/pipx/) (or pip):

```sh
$ pipx install slackoff
```
or add it to your [Poetry](https://python-poetry.org/docs/) project:

```sh
$ poetry add slackoff
```

# Usage

After installation, automatically sign out of a Slack workspace:

```sh
$ slackoff My Workspace Name
```

or sign back in:

```sh
$ slackoff My Workspace Name
```
