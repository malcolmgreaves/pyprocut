import argparse
from datetime import datetime
from pathlib import Path

from {{cookiecutter.package_name}}.utils import (
    make_logger,
    filename_wo_ext,
    program_init_param_msg,
    evenly_space,
)

logger = make_logger(filename_wo_ext(__file__))

_NAME = "{{cookiecutter.repo_name}} model server"

def main(
    model_path: Path,
    config_path: Path,
    log_level: str,
) -> None:
    program_init_param_msg(
        logger,
        evenly_space([
            ("Model filepath", model_path),
            ("Configuration", config_path),
            ("Logging level", log_level),

        ]),
        _NAME,
        log_each_line=False,
    )
    logger.setLevel(log_level)
    if not model_path.is_file():
        raise ValueError("No model file present.")
    if not config_path.is_file():
        raise ValueError("No configuration file present.")

    start = datetime.now()
    logger.fatal("TODO: load model")
    logger.fatal("TODO: load & parse configuration file")
    logger.fatal("TODO: initialize server")
    logger.info(f"({datetime.now() - start}) finished initializing model server")

    logger.fatal("TODO: listen & respond for requests")

    raise ValueError("TODO: implement model server")


def entrypoint() -> None:
    parser = argparse.ArgumentParser(description=_NAME,)
    parser.add_argument(
        "--model-path",
        type=str,
        help="Filepath for serialized model",
        required=True,
    )
    parser.add_argument(
        "--config-path",
        type=str,
        help="Path to configuration file.",
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
        config_path=Path(args.config_path),
        log_level=args.log_level,
    )


if "__main__" == __name__:
    entrypoint()
