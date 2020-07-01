#!/bin/bash

echo "-----------------------------------"
echo "| Project Template Creation Tests |"
echo "-----------------------------------"

set -euo pipefail

# alias sh='/bin/bash'
# alias ash='/bin/bash'
# alias pip='/usr/bin/pip3'
# alias python='/usr/bin/python3'

# TODO [MG] Still an issue? # BUG: Aliases don't work in alpine linux & py36???

#
# NOTE: These array values *must* equal the *exact* string values, in order,
#       for the project_type template variable defined in cookiecutter.json.
#
declare -a PROJECT_TYPES=(
    "python_lib: A pip-installable python3 Library"
    "docker_exe: An executable buildable with Docker"
)
END=$((${#PROJECT_TYPES[@]}-1))


EXAMPLE_REPO_NAME="template_project_0"
TESTING_CC_DIR="testing_cookiecutter_template"

echo "Making testing dir: ${TESTING_CC_DIR}"
mkdir "${TESTING_CC_DIR}"
pushd "${TESTING_CC_DIR}"

for PTYPE in $(seq 0 ${END});
do
  echo "Testing project template creation for project type: ${PTYPE}"
  PROJECT_TYPE=${PROJECT_TYPES[${PTYPE}]}
  echo "${PROJECT_TYPE}"
  echo "---------------------------------------------------------"
  echo ""

  if [[ "${PTYPE}" == "0" ]]; then
    echo "Creating project locally"
    echo "------------------------"

    cookiecutter ../ \
      --no-input \
      repo_name="${EXAMPLE_REPO_NAME}" \
      package_name="a_package_${PTYPE}" \
      project_type="${PROJECT_TYPE}"

    pushd "${EXAMPLE_REPO_NAME}"
    echo "-----------------------------------------"

    echo "Installing template project code & dependencies"
    echo "--"
    poetry install
    echo "-----------------------------------------"

    echo "Sanity-checking template project"
    echo "--"
    poetry run pytest -v --cov-branch
    echo "-----------------------------------------"
    popd
  fi

  if [[ "${PTYPE}" == "1" ]];
  then
    echo "Building docker image for executable project"
    echo "--"
    NAME="docker_exe"
    docker build . -t "${NAME}"
    echo "-----------------------------------------"

    echo "Testing default TODO command: --help flag must work."
    echo "--"
    docker run "${NAME}" TODO_main_program -h
    echo "-----------------------------------------"
  fi
  popd
done

popd
rm -rf "${TESTING_CC_DIR}"
echo "Cleaned-up testing dir: ${TESTING_CC_DIR}"