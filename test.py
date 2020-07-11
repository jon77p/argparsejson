from argparsejson import argparsejson

if __name__ == "__main__":
    parser = argparsejson.parse_arguments("example_commands.json")
    parser.parse_args()
