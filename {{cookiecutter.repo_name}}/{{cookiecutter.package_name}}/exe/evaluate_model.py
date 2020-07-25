import argparse
from datetime import datetime
from pathlib import Path

from {{cookiecutter.package_name}}.utils import (
    make_logger,
    filename_wo_ext,
    program_init_param_msg,
    evenly_space,
    ensure_write_path,
)

logger = make_logger(filename_wo_ext(__file__))

_NAME = "{{cookiecutter.repo_name}} model evaluation"

def main(
    model_path: Path,
    test_dir: Path,
    eval_path: Path,
    log_level: str,
) -> None:
    program_init_param_msg(
        logger,
        evenly_space([
            ("Model filepath", model_path),
            ("Testing data", test_dir),
            ("Evaluation filepath", eval_path),
            ("Logging level", log_level),

        ]),
        _NAME,
        log_each_line=False,
    )
    logger.setLevel(log_level)
    if not model_path.is_file():
        raise ValueError("Model file doesn't exist.")
    if not test_dir.is_dir():
        raise ValueError("Test data directory doesn't exist.")
    ensure_write_path(eval_path)

    start = datetime.now()

    logger.info(f"({datetime.now() - start}) evaluated models")
    raise ValueError("TODO: logic for performing model evaluation")


def entrypoint() -> None:
    parser = argparse.ArgumentParser(description=_NAME,)
    parser.add_argument(
        "--model-path",
        type=str,
        help="Filepath for serialized model",
        required=True,
    )
    parser.add_argument(
        "--test-dir",
        type=str,
        help="Path to directory containing testing data.",
        required=True,
    )
    parser.add_argument(
        "--eval-path",
        type=str,
        help="Filepath to save evaluation data, JSON format.",
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
        model_path=Path(args.model_path),
        test_dir=Path(args.test_dir),
        eval_path=Path(args.eval_path),
        log_level=args.log_level,
    )


if "__main__" == __name__:
    entrypoint()
