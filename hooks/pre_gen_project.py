import re
import string
from typing import Sequence


def assert_name_properites(
    name: str, message_prefix: str, ok_punctuation: Sequence[str] = ()
) -> None:
    assert isinstance(name, str), f"{message_prefix} must be a string.".capitalize()

    assert len(name) > 0, f"{message_prefix} must be non-empty.".capitalize()

    assert name.lower() == name, f"{message_prefix} must be all lower case"

    assert " " not in name, f"{message_prefix} cannot have spaces.".capitalize()

    bad_punct = string.punctuation
    for keep_punct in ok_punctuation:
        bad_punct = bad_punct.replace(keep_punct, "")
    for not_allowed in bad_punct:
        assert (
            not_allowed not in name
        ), f"{message_prefix} must *not* contain punctuation '{not_allowed}'.".capitalize()

    assert (
        re.match("[a-z]", name[0]) is not None
    ), f"{message_prefix} must sta rt with a letter, not '{name[0]}'.".capitalize()


def entrypoint():
    assert_name_properites(
        name="{{cookiecutter.repo_name}}",
        message_prefix="repository name",
        ok_punctuation=["-"],
    )
    assert_name_properites(
        name="{{cookiecutter.package_name}}",
        message_prefix="package name",
        ok_punctuation=["_"],
    )


if __name__ == "s__main__":
    entrypoint()
