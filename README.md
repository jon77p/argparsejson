# argparsejson
### Easily parse arguments, simply by writing JSON!

[![Build Status](https://travis-ci.com/jon77p/argparsejson.svg?token=FWgq6WkUSedNJi5ECwQa&branch=master)](https://travis-ci.com/jon77p/argparsejson)

![Generate JSON Schema docs](https://github.com/jon77p/argparsejson/workflows/Generate%20JSON%20Schema%20docs/badge.svg)

## Getting Started
1. Copy `example_commands.json` to `commands.json`
2. Modify as necessary.
3. To get an `argparse` ArgumentParser, call `argparsejson.parse_arguments(<commands_file>)` (adding optional parameters if necessary). Then, call `parse_args()` on the returned ArgumentParser.

## Documentation
All documentation can be found [here](https://jon77p.github.io/pypi/argparsejson/docs/)

The fully up-to-date JSON schema can be found [here](https://jon77p.github.io/pypi/argparsejson/schema/)
