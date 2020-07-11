# argparsejson
### Easily parse arguments, simply by writing JSON!
## Getting Started
1. Copy `example_commands.json` to `commands.json`
2. Modify as necessary.
3. To get an `argparse` ArgumentParser, call `argparsejson.parse_arguments(<commands_file>)` (adding optional parameters if necessary). Then, call `parse_args()` on the returned ArgumentParser.
