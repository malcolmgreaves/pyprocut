import argparse
from typing import Optional

from {{cookiecutter.package_name}}.utils import make_logger, filename_wo_ext


logger = make_logger(filename_wo_ext(__file__))

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
    logger.fatal(
        "TODO print out your cmd-line arguments after parsing: log arguments used for program"
    )
    logger.fatal(f"TODO argument_name: {argument_name}")


if __name__ == "__main__":
    entrypoint()
