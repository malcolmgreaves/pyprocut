import os
from pathlib import Path
from typing import Mapping, Iterable, Sequence, Union


def reorganize_files_for_project_type(
    project_type_input: str, verbose: bool = False
) -> None:
    if project_type_input.startswith("python_lib"):
        print("Project setup for a pip-installable Python library")
        handle_python_lib_project(verbose=verbose)

    elif project_type_input.startswith("docker_exe"):
        print("Project setup for Docker buildable executable")
        handle_docker_exe_project(verbose=verbose)

    elif project_type_input.startswith("ml"):
        print("Project setup for machine learning project")
        handle_ml_project(verbose=verbose)

    else:
        raise ValueError(
            f"Cannot parse string into a recognized project type.\n"
            f"Unexpected project type input:   '{project_type_input}'\n"
            f"Does not match known values for: '[Python Library, Docker Executable]'"
        )
    print(
        "--------------------------------------------------------------------------------------------------------\n"
        ">> Post Creation Next Steps <<\n"
        "   1. Move into your new project!\n"
        "   2. Make a git repository in '{{cookiecutter.repo_name}}'.\n"
        "   3. Add your GitHub repository as a remote.\n"
        "   4. Make an initial commit.\n"
        "   5. Push changes to the `main` branch.\n"
        "   6. Find all 'TODO's and fix or otherwise update appropriately!\n"
        "-----------------------------------------------------------------\n"
        "```\n"
        "cd {{cookiecutter.repo_name}}\n"
        "git init\n"
        "git remote add origin git@github.com:{{cookiecutter.user}}/{{cookiecutter.repo_name}}.git\n"
        "git add . && git commit -a -m 'Initial commit from template'\n"
        "git branch -m main && git push -u origin main\n"
        "find . -type f | grep TODO && find . -type f | xargs grep TODO\n"
        "```\n"
        "--------------------------------------------------------------------------------------------------------"
    )


def handle_python_lib_project(verbose: bool = False) -> None:
    remove(
        map(
            path,
            [
                # docker_exe specific files
                "Dockerfile.docker_exe",
            ],
        ),
        verbose=verbose,
    )


def handle_docker_exe_project(verbose: bool = False) -> None:
    rename(
        {
            path("Dockerfile.docker_exe"): path("Dockerfile"),
        },
        verbose=verbose,
    )

def handle_ml_project(verbose: bool = False) -> None:
    remove(
        map(
            path,
            [
                # python_lib / docker_exe specific files
                ("src", "{{cookiecutter.package_name}}", "exe", "TODO_main_program.py"),
            ],
        ),
        verbose=verbose,
    )
    rename(
        {
            path("Dockerfile.docker_exe"): path("Dockerfile"),
        },
        verbose=verbose,
    )


def path(path_parts: Union[str, Sequence[str]]) -> Path:
    """Construct a path from one or more parts, starting from the current directory '.'
    """
    if isinstance(path_parts, str):
        return Path(".") / path_parts
    elif isinstance(path_parts, Sequence):
        complete_path = Path(".")
        for p in path_parts:
            complete_path = complete_path / p
        return complete_path
    else:
        raise TypeError(
            "Expecting either a single path part (str) or a "
            "sequence of path parts (Sequence[str]). Received "
            f"instead a {type(path_parts)}: '{path_parts}'"
        )


def rename(orig2new: Mapping[Path, Path], verbose: bool = False) -> None:
    """Renames a set of files: keys are existing names and their value is the new name.

    :raises IOError
    """
    for old, new in orig2new.items():
        o, n = str(old.absolute()), str(new.absolute())
        if verbose:
            print(f"Renaming '{o}' to '{n}'")
        try:
            os.rename(o, n)
        except:
            print(f"ERROR: Could not rename '{o}' to '{n}'")
            raise


def remove(removing: Iterable[Path], verbose: bool = False) -> None:
    """Removes the files from the underlying filesystem.

    :raises IOError
    """
    for f in removing:
        if verbose:
            print(f"Removing '{str(f.absolute())}'")
        try:
            delete(f)
        except:
            print(f"ERROR: Could not remove '{f.absolute()}'")
            raise


def delete(p: Path) -> None:
    """Deletes the file or directory located at the specified path.
    """
    if p.is_dir():
        for f in os.listdir(str(p.absolute())):
            delete(p / f)
        p.rmdir()
    elif p.is_file():
        p.unlink()
    else:
        print(f"WARNING: Cannot delete non-existent path. Doing nothing.")


def append(
    source2dest: Mapping[Path, Path], remove_after: bool, verbose: bool = False
) -> None:
    """Append all of the contents from each key `source` to its corresponding value `destination`.

    :raises IOError
    """
    for source, destination in source2dest.items():
        if verbose:
            print(
                f"Appending the contents of '{source.absolute()}' to '{destination.absolute()}'"
            )
        try:
            with open(str(source.absolute()), "rt") as r:
                with open(str(destination.absolute()), "a") as w:
                    for line in r:
                        w.write(line)
            if remove_after:
                if verbose:
                    print("Removing source since its contents were appended.")
                source.unlink()
        except:
            print(f"ERROR: Could not append '{source}' to '{destination}'")
            raise


def entrypoint():
    reorganize_files_for_project_type(
        project_type_input="{{cookiecutter.project_type}}", verbose=False
    )


if __name__ == "__main__":
    entrypoint()
