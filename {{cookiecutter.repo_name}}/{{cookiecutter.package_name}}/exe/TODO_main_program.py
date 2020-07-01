import argparse
from typing import Optional


def entrypoint():
    parser = argparse.ArgumentParser(
        description="TODO: implement your main function here"
    )
    parser.add_argument(
        "--argument-name",
        type=str,
        help="TODO add command line arguments to your exe",
        default=None,
    )
    args = parser.parse_args()
    argument_name: Optional[str] = args.argument_name
    print(
        "TODO print out your cmd-line arguments after parsing: log arguments used for program"
    )
    print(f"argument_name: {argument_name}")


if __name__ == "__main__":
    entrypoint()
