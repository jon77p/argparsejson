import argparse
import copy
import json
import os

def getType(s:str):
    if s is None:
        return

    if type(s) != str:
        return type(s)

    s = s.lower()

    if s == "int" or s == "integer":
        return int
    elif s == "bool" or s == "boolean":
        return bool
    elif s == "str" or s == "string":
        return str
    elif s == "float":
        return float
    else:
        return None

class MyArgParser(argparse.ArgumentParser):
    def __init__(self, prog=None, add_help=True):
        self.add_help=add_help
        super().__init__(prog=prog, add_help=add_help)

    def exit(self, status=0, message=None):
        if status:
            if self.add_help:
                super().exit(status=status, message=message)

def parse_arguments(commands_file, isClient=False, allowJson=False, prog=None, add_help=True):
    parser = MyArgParser(prog=prog, add_help=add_help)

    if not isClient:
        parser.add_argument("--debug", action='store_true')

        parser.add_argument("-i", action='store_true')

    if allowJson:
        parser.add_argument("--json", action='store_true', default=False)

    subparsers = parser.add_subparsers(dest="action")
    help_parser = subparsers.add_parser("help", help="show this help message")
    usage_parser = subparsers.add_parser("usage", help="show this usage message")

    implemented = json.load(open(os.path.abspath(commands_file), "r"))

    for cmd in implemented:
        aliases = [cmd.get('abbrev')] if cmd.get('abbrev') is not None else []
        sub_parser = subparsers.add_parser(cmd.get('name'), aliases=aliases, add_help=True)

        for a in cmd.get('args', []):
            kwargs = copy.deepcopy(a)
            for k in kwargs.keys():
                if k not in ["name", "abbrev", "action", "nargs", "const", "default", "type", "choices", "required", "help", "metavar", "dest"]:
                    raise ValueError("'{}' is an unexpected keyword argument for argparse".format(k))

            abbrev = kwargs.pop('abbrev') if kwargs.get('abbrev') is not None else None
            name = kwargs.pop('name') if kwargs.get('name') is not None else None

            if kwargs.get('type') is not None:
                kwargs['type'] = getType(kwargs.get('type'))

            if kwargs.get("action") == "store_true":
                if kwargs.get("type") is not None:
                    del kwargs["type"]
                if kwargs.get("default") is not None:
                    del kwargs["default"]

            if abbrev is None:
                args = [name]
            else:
                args = [abbrev, name]

            sub_parser.add_argument(*args, **kwargs)

    return parser
