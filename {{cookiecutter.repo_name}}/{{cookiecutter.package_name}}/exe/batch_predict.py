import argparse
import os
import traceback
from datetime import datetime
from pathlib import Path

from tqdm import tqdm

from {{cookiecutter.package_name}}.utils import (
    make_logger,
    filename_wo_ext,
    program_init_param_msg,
    evenly_space,
    ensure_output_dir,
)

logger = make_logger(filename_wo_ext(__file__))


_NAME = "{{cookiecutter.repo_name}} batch processing"

def main(
    model_path: Path,
    input_dir: Path,
    output_dir: Path,
    log_level: str,
) -> None:
    program_init_param_msg(
        logger,
        evenly_space([
            ("Model filepath", model_path),
            ("Input data", input_dir),
            ("Output predictions", output_dir),
            ("Logging level", log_level),

        ]),
        _NAME,
        log_each_line=False,
    )
    logger.setLevel(log_level)
    if not input_dir.is_dir():
        raise ValueError("Input directory doesn't exist.")
    ensure_output_dir(output_dir)

    start = datetime.now()

    logger.fatal("TODO: load model from filepath")
    logger.info(f"({datetime.now() - start}) loaded model")

    input_files = os.listdir(str(input_dir))
    logger.info(f"Batch processing {len(input_files)} files")
    n_success, n_fail = 0, 0

    for i_fname in tqdm(input_files, total=len(input_files)):
        input_filename = str(input_dir / i_fname)
        try:
            logger.fatal("TODO: logic for loading input data and predicting")
            with open(str(output_dir / f"{i_fname}.json"), "wt") as wt:
                logger.fatal("TODO: logic for writing prediction to disk")
            n_success += 1
        except Exception as e:
            logger.error(
                f"[SKIP] Could not handle '{input_filename}' due to '{e}'"
            )
            traceback.print_exc()
            n_fail += 1
        raise ValueError("TODO: update batch prediction script")

    logger.info(
        f"({datetime.now() - start}) done, with {n_success} successes and {n_fail} failures"
    )


def entrypoint() -> None:
    parser = argparse.ArgumentParser(description=_NAME,)
    parser.add_argument(
        "--model-path",
        type=str,
        help="Filepath to serialized model",
        required=True,
    )
    parser.add_argument(
        "--input-dir",
        type=str,
        help="Path to directory containing input files that need predictions.",
        required=True,
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        help="Path to directory containing model predictions. 1:1 mapping with input files.",
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
        input_dir=Path(args.input_dir),
        output_dir=Path(args.output_dir),
        log_level=args.log_level,
    )


if "__main__" == __name__:
    entrypoint()
