import argparse
from datetime import datetime
from pathlib import Path

from {{cookiecutter.package_name}}.utils import (
    make_logger,
    filename_wo_ext,
    program_init_param_msg,
    evenly_space,
    ensure_output_dir,
)

logger = make_logger(filename_wo_ext(__file__))

_NAME = "{{cookiecutter.repo_name}} formatting data"

def main(
    input_dir: Path,
    output_dir: Path,
    log_level: str,
) -> None:
    program_init_param_msg(
        logger,
        evenly_space([
            ("Input data", input_dir),
            ("Formatted", output_dir),
            ("Logging level", log_level),

        ]),
        _NAME,
        log_each_line=False,
    )
    logger.setLevel(log_level)
    if not input_dir.is_dir():
        raise ValueError("Input data directory doesn't exist.")
    ensure_output_dir(output_dir)

    start = datetime.now()

    logger.info(f"({datetime.now() - start}) formatted data")
    raise ValueError("TODO: logic for formatting data")


def entrypoint() -> None:
    parser = argparse.ArgumentParser(description=_NAME,)
    parser.add_argument(
        "--input-dir",
        type=str,
        help="Path to directory containing input data.",
        required=True,
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        help="Output directory for formatted data.",
        required=True,
    )
    parser.add_argument(
        "--log-level",
        type=str,
        help="Logging level to use. One of: {DEBUG, INFO, WARNING, FATAL}. Defaults to INFO.",
        default="INFO",
    )

    args = parser.parse_args()
    main(
        input_dir=Path(args.input_dir),
        output_dir=Path(args.output_dir),
        log_level=args.log_level,
    )


if "__main__" == __name__:
    entrypoint()
