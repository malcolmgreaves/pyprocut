from typing import Sequence
from pathlib import Path

from pytest import fixture, raises, mark

from {{cookiecutter.package_name}}.TODO_write_your_own_module import TODO


# options for scope are: 'session', 'module', or completely omit for per-use invocation
@fixture(scope="module")
def a_testing_resource(resources: Path) -> Sequence[str]:
    return (
        "TODO - write your own fixutres and tests! "
        "You can use the `resources` fixture defined in conftest.py "
        "to give you easy access to loading resource files for your own tests."
    )


# Test functions _MUST_ start with "test_"
# Using a fixture is as simple as including it by name in the test function's parameter list!


def test_using_simple_fixture(a_testing_resource):
    assert "TODO - write your own fixutres and tests!" in a_testing_resource


def test_resources_fixture(resources):
    # You can define global @fixtures in the conftest.py file.
    assert resources.is_dir()
    assert str(resources).endswith("tests/resources")


def test_fn_raises_err():
    with raises(ValueError):
        raise ValueError


def test_module_fn():
    assert TODO() == "Hello world!"


@mark.skip(reason="TODO need to write your own tests :D")
def test_skipped_fn():
    raise NotImplementedError("See https://docs.pytest.org/en/latest/skipping.html for "
                              "documentation on skipping, e.g. @skipif")