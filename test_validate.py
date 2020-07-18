from argparsejson import argparsejson
import pytest

def validate():
    return argparsejson.parse_arguments("example_commands.json")

def test_validate():
    parser = validate()
    assert isinstance(parser, argparsejson.MyArgParser)

def test_parser_creation():
    parser = validate()
    assert parser.prog == 'pytest'

def test_arg_parsing_empty():
    parser = validate()
    with pytest.raises(SystemExit) as status_code:
        parser.parse_args(args=[])

    assert status_code.value.code == 2

def test_arg_parsing_help():
    parser = validate()
    with pytest.raises(SystemExit) as status_code:
        parser.parse_args(args=["-h"])

    assert status_code.value.code == 2

def test_arg_parsing():
    parser = validate()
    result = parser.parse_args(args=["sc", "param"])

    assert result.action == 'sc'
