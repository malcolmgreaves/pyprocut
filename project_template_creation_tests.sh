#!/bin/bash

echo "-----------------------------------"
echo "| Project Template Creation Tests |"
echo "-----------------------------------"

set -euo pipefail

#
# NOTE: These array values *must* equal the *exact* string values, in order,
#       for the project_type template variable defined in cookiecutter.json.
#
declare -a PROJECT_TYPES=(
    "python_lib: A pip-installable python3 Library"
    "docker_exe: An executable buildable with Docker"
    "ml: A machine learning project, with HTTP server in Docker"
)
END=$((${#PROJECT_TYPES[@]}-1))


EXAMPLE_REPO_NAME="template_project_0"
TESTING_CC_DIR="testing_cookiecutter_template"

echo "Making testing dir: ${TESTING_CC_DIR}"
mkdir "${TESTING_CC_DIR}"
cd "${TESTING_CC_DIR}"

for PTYPE in $(seq 0 ${END});
do
  echo "Testing project template creation for project type: ${PTYPE}"
  PROJECT_TYPE=${PROJECT_TYPES[${PTYPE}]}
  echo "${PROJECT_TYPE}"
  echo "---------------------------------------------------------"
  echo ""

  cookiecutter ../ \
    --no-input \
    repo_name="${EXAMPLE_REPO_NAME}" \
    package_name="a_package_${PTYPE}" \
    project_type="${PROJECT_TYPE}" \
    user="a_gh_username"

  cd "${EXAMPLE_REPO_NAME}"

  if [[ "${PTYPE}" == "0" ]]; then
    echo "Installing template project code & dependencies"
    echo "--"
    poetry install
    echo "-----------------------------------------"

    echo "Sanity-checking template project"
    echo "--"
    poetry run pytest -v --cov-branch
    echo "-----------------------------------------"
  fi

  if [[ "${PTYPE}" == "1" ]];
  then
    echo "Building docker image for executable project"
    echo "--"
    NAME="docker_exe"
    docker build -t "${NAME}" .
    echo "-----------------------------------------"

    echo "Testing default TODO command: --help flag must work."
    echo "--"
    docker run "${NAME}" --help
    echo "-----------------------------------------"
  fi

  if [[ "${PTYPE}" == "2" ]];
  then
    echo "Installing ML project dependencies"
    echo "--"
    poetry install
    echo "-----------------------------------------"

    echo "Testing that ML project scripts exist"
    echo "--"
    for cmd in $(echo download format-data make-train train evaluate predict serve); do
      echo "Testing help flag for ${cmd}"
      echo '-'
      poetry run "${cmd}" --help
      echo "------"
    done
    echo "-----------------------------------------"

    echo "Testing that docker build works for ML project"
    echo "--"
    NAME="docker_exe"
    docker build -t "${NAME}" .
    echo "-----------------------------------------"

    echo "Testing docker image for ML project: --help flag must work."
    echo "--"
    docker run "${NAME}" --help
    echo "-----------------------------------------"
  fi

  cd ..
  rm -rf "${EXAMPLE_REPO_NAME}"
done

cd ..
rm -rf "${TESTING_CC_DIR}"
echo "Cleaned-up testing dir: ${TESTING_CC_DIR}"
