# Release
This document details how {{cookiecutter.repo_name}} is published and released.


## Publishing Automation & Releases
This project's CI is set to automatically perform development releases of the project on every successful merge to `main`. As the final step of the CI pipeline, this action only occurs after all type checking, linting, unit & integration testing, and other verification steps for the project have been completed.

We use `git tag`s to denote project releases. Every published release of this project  _must_ have a corresponding tag that is equal to the published version.

Versions **MUST** conform to [Sematic Versioning 2.0](https://semver.org/)  rules. Any 0.x.x release is considered experimental and, as a result, may allow breaking changes between any two versions.


## Release Instructions
To cut a new release, push a tag of the project's version on `main`:
```bash
git checkout main && git tag $(poetry version | cut -d" " -f) && git push --tags
```
NOTE: Before tagging a commit, ensure that it is up-to-date on the repo. These actions trigger a build on CI that will publish a release of `{{cookiecutter.repo_name}}`.

TODO: Set-up CI with your repository (e.g. )

## Python Library Release
Since this project is a Python library, its version is defined within the `pyproject.toml` file and interpreted `poetry`. Other than inspecting the file, the version value is accessible via 
the command line:
```bash
poetry version
```

To perform a manual package publish to PyPI, do the following:
```bash
poetry build && poetry publish
```
