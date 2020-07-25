import argparse
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

from {{cookiecutter.package_name}}.utils import (
    make_logger,
    filename_wo_ext,
    program_init_param_msg,
    evenly_space,
    ensure_write_path,
)

logger = make_logger(filename_wo_ext(__file__))

_NAME = "{{cookiecutter.repo_name}} model training"

def main(
    model_path: Path,
    train_dir: Path,
    test_dir: Optional[Path],
    eval_path: Path,
    log_level: str,
) -> None:
    program_init_param_msg(
        logger,
        evenly_space([
            ("Model filepath", model_path),
            ("Training data", train_dir),
            ("Testing data", test_dir),
            ("Evaluation filepath", eval_path),
            ("Logging level", log_level),

        ]),
        _NAME,
        log_each_line=False,
    )
    logger.setLevel(log_level)
    ensure_write_path(model_path)
    if not train_dir.is_dir():
        raise ValueError("Training data directory doesn't exist.")
    if test_dir and not test_dir.is_dir():
        raise ValueError("Testing data directory doesn't exist.")
    ensure_write_path(eval_path)

    start = datetime.now()

    logger.fatal("TODO: initialize model")

    train_files = os.listdir(str(train_dir))
    logger.info(f"Training model on {len(train_files)} files")

    if test_dir:
        test_files = os.listdir(str(test_dir))
        logger.info(f"Testing model on {len(test_files)} files")
    else:
        logger.warning(f"No testing data supplied.")

    logger.info(f"({datetime.now() - start}) completed training")
    raise ValueError("TODO: implement training logic")


def entrypoint() -> None:
    parser = argparse.ArgumentParser(description=_NAME,)
    parser.add_argument(
        "--model-path",
        type=str,
        help="Filepath for serialized model",
        required=True,
    )
    parser.add_argument(
        "--train-dir",
        type=str,
        help="Path to directory containing training data.",
        required=True,
    )
    parser.add_argument(
        "--test-dir",
        type=str,
        help="Path to directory containing testing data.",
        default=None,
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
        train_dir=Path(args.train_dir),
        test_dir=Path(args.test_dir) if args.test_dir else None,
        eval_path=Path(args.eval_path),
        log_level=args.log_level,
    )


if "__main__" == __name__:
    entrypoint()
