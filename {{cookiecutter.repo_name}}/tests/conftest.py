from pathlib import Path

from pytest import fixture


@fixture(scope="session")
def resources() -> Path:
    return (Path(".") / "tests" / "resources").absolute()

# TODO Useful to make fixtures here that load up test data or test 
#      configs defined in the "tests/resources" directory.
#      Or, for other global, needed by all/most/many testing resources.
