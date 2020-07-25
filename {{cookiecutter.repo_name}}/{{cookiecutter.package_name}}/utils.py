import logging
import os
import shutil
from pathlib import Path
from typing import Sequence, Optional, Tuple, Any


def make_logger(name: str, log_level: int = logging.INFO) -> logging.Logger:
    """Create a logger using the given :param:`name` and logging level.
    """
    if name is None or not isinstance(name, str) or len(name) == 0:
        raise ValueError("Name must be a non-empty string.")
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logging.basicConfig(
        format="%(asctime)s %(levelname)s [%(name)s] - %(message)s",
    )
    return logger


def filename_wo_ext(filename: str) -> str:
    """Gets the filename, without the file extension, if present.
    """
    return os.path.split(filename)[1].split(".", 1)[0]


def program_init_param_msg(
    logger: logging.Logger,
    msg: Sequence[str],
    name: Optional[str] = None,
    log_each_line: bool = False,
) -> None:
    """Pretty prints important, configurable values for command-line programs.

    Uses the :param:`logger` to output all messages in :param:`msg`.

    If :param:`log_each_line` is true, then each message is applied to `logger.info`.
    Otherwise, a newline is inserted between all messages and they are all logged once.

    If :param:`name` is supplied, then it is the first logged message. If there is no
    name and the function is logging all messages at once, then a single newline is
    inserted before the mass of messages.
    """
    separator: str = max(map(len, msg)) * "-"
    if log_each_line:
        logger.info(separator)
        if name is not None:
            logger.info(name)
        for line in msg:
            logger.info(line)
        logger.info(separator)
    else:
        if name:
            starting = f"{name}\n"
        else:
            starting = "\n"
        logger.info(starting + "\n".join([separator] + list(msg) + [separator]))


def evenly_space(name_and_value: Sequence[Tuple[str, Any]]) -> Sequence[str]:
    """Pads the middle of (name,value) pairs such that all values vertically align.

    Adds a ':' after each name (first element of each tuple).
    """
    if len(name_and_value) == 0:
        return []
    max_name_len = max(map(lambda x: len(x[0]), name_and_value))
    vs = []
    for name, value in name_and_value:
        len_spacing = max_name_len - len(name)
        spacing = " " * len_spacing
        vs.append(f"{name}: {spacing}{value}")
    return vs


def ensure_write_path(output_filepath: Path) -> None:
    """Ensures that the supplied path is a writeable file: raises an Error if not.
    """
    if output_filepath.is_dir():
        raise ValueError(f"Output filepath is a directory: {output_filepath}")
    if output_filepath.is_file():
        os.remove(str(output_filepath))
    output_filepath.mkdir(parents=True, exist_ok=True)
    output_filepath.rmdir()
    output_filepath.touch()


def ensure_output_dir(output_dir: Path) -> None:
    """Ensures that there is a clean, empty directory at the supplied path.
    """
    if output_dir.is_dir():
        shutil.rmtree(str(output_dir))
    output_dir.mkdir(parents=True, exist_ok=True)
