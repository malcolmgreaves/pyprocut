# pyprocut
Cookiecutter template for python projects. Includes support for:
+ Python libraries
+ Docker-buildable projects




## Instructions
Make sure you either have `cookiecutter`
[installed system-wide](https://cookiecutter.readthedocs.io/en/latest/installation.html#alternate-installations). For example, using [`pipx`](https://github.com/pipxproject/pipx), we can install as:
```bash
pipx install cookiecutter
```
And use in this (and any other) project. 


When making a new Python library or service, point `cookiecutter` to this 
template repository upon invoking (a local filepath works as well):
```bash
cookiecutter git@github.com/malcolmgreaves/pyprocut.git
```
You will also need to [supply values for the project's template variables](#filling-template-variables). 
When prompted for the `project_types` variable, there are **three** distinct choices, 
one of which is selectable via supplying the associated number [1-3]:
1. `python_lib`: A pip-installable python library.
2. `docker_exe`: A Docker buildable image & associated Python executable program.




## Post-Clone Steps: Handle TODOs
After creating a new project using this template, be sure to replace all
instances of **TODO** with something that's appropratie for your project.
Check the README, src/, and tests/ for files that need per-project 
customization. E.g. you may want to delete the templated tests and package 
module and write your own from scratch! They are there as a tiny reference on
using `pytest` and having proper Python project package & directory structure.




## General Pan-Project Documentation
Included in this project template repository is general documentation that is applicable to many projects:

The `Development Tools Installation` page documents how to install common system librarires and tools used 
across development projects.

The `Software Engineering Hygiene for Data Scientists` page guides data scientists in honing their software 
crafting skills to produce high quality, reusable, robust programs.

The `Coding Style` page serves as a coherent document outlining standards and explaining their purpose and 
intended effect in producing readable, understandable code.



## Working with cookiecutter
`cookiecutter` has several conventions and expected behaviors that, once understood,
make working with the tool and an assoicated project template pleasant & straightforward.   


### Filling Template Variables
Template variables form the foundation of template project creation with `cookiecutter`. 
Variables may be supplied by three distinct routes:

1. Via STDIN: default `cookiecutter` project behavior is to prompt the user with the variable's name
and description and interactively ask the caller to fill-in the value.  

2. Via the command line. Add the `--no-input` flag to prevent reading from STDIN and supply
template variable values as command line arguments. Each variable is specified by the syntax:
```bash
cookiecutter ... --no-input VARIABLE=VALUE
``` 
Where `VARIABLE` is the variable name and `VALUE` is the literal value to be used.

3. As a YAML configuration file. Along with `--no-input`, add a path to a YAML file
using `--config-file`. This file must, under the key / scope `default_context`, lust
each template variable and configured value. The syntax of the file is:
```yaml
default_context:
    VARIABLE: VALUE
```


### Project Creation Recipe
When creating a new project from a template repository, the recipe `cookiecutter` follows is:

1. **Use `git` to `clone` this repository and grab the contents of the  `{{cookiecutter.repo_name}}` directory.**
By default, `cookiecutter` caches the repository under `~/.cookiecutters`. The folder is copied to 
the current working directory.

2. **Ask the user to instantiate _template values_: default behavior prompts on STDIN.**
The [`cookiecutter.json`](./cookiecutter.json) file defines an object: the object's fields are
the template variable names and their values serve as user prompts for the required information.
A list of values means that the user must choose one of the listed values by entering in one
more than the value's list index. The [fiilliing template variables](#filling-template-variables)
section details how to supply template variable values without using STDIN.
   
3. **Run the pre generation hook: `hooks/pre_gen_project.py`.** This program validates the
template variable input. It ensures that the repository name (`repo_name`) is valid for Gitlab.
And that the initial package name (`package_name`) is a valid Python name. The project type is
also validated, ensuring that it is a known option. This program must exit with a successful
status code, otherwise project creation is aborted and files are cleaned up.

4. **Instantiate all uses of project template variables with user-supplied values.** 
Additionally, `cookiecutter` **evaluates all conditional statements**. For more details on what
these mean, see the [evaluating-template-variables](#evaluating-template-variables) section.

4. **Run the post generation hook: `hooks/post_gen_project.py`.** After validation, this 
hook program inspects the selected `project_type` and manipulates files in the cloned project 
directory. Files extraneous to the specific project type are removed; the relevant ones are 
renamed to common, idomatic names (e.g. `.travis.yml` and `Dockerfile`). And any additional
file content is appended to existing project files.


### Evaluating Template Variables
Once variables are supplied and validated by the pre-generation hook, their use in project files
is replaced by their values. This means evey variable use syntax, i.e.:
```jinja2
{{cookiecutter.VARIABLE}}
``` 
is replaced with the literal `VALUE` supplied earlier.

Moreover, all conditional templating expressions are evaluated. These expressions allow for
different blocks of code to be present in a given file, depending on the `VALUE` for a 
particular `VARIABLE`. For instance, given the following conditional:
```jinja2
{% if cookiecutter.VARIABLE == "1" %}

    associated text when the value 
    supplied for VARIABLE is "1"

{% elif cookiecutter.DIFFERENT_VARIABLE == "new value" %}

    completely different block of text
    unrelated to the first block
    present if a different variable,
    DIFFERENT_VARIABLE, equals "new value"
    
{% else %}

    if VARIABLE and DIFFERENT_VARIABLE are not 
    equal to the values specified above, 
    then this block of text is inserted

{% endif %}
```
There are three different blocks of code that could potentially remain after the conditional
expression is evaluated. The statements are evaluated top-to-bottom: different variables may
be checked in this conditional. The first test to pass has its associated text block inserted
directly into the file precisely between the last `%}` and `{%` character sequences. All other 
parts of the conditional expression, the other branch bodies & their associated boolean tests,
are removed.

Note that simple conditional statements are supported as well. E.g. only a single variable-value
pair may be evaluated to potentially insert a solitary block of code:
```jinja2
program_value = {
    "key_1": "value_1" {% if len(cookiecutter.second_key) > 0 %}
    "key_2": "{{cookiecutter.second_key}}", {% endif %}
}
```
Would insert the user-supplied value for `second_key` into the dictionary iff the value was non-
empty i.e. supplied by the user. Otherwise, the dictionary `program_value` would only haven the
single key-value pair: `"key_1"` with `"value_1"`. Note the placement of the if-statement: if the
test and end-if were on separate lines, then there would be blank lines surrounding the inserted
`"key_2"` value assignment.




## Development Setup
If you're working on _this_ template repoistory, ensure you have `poetry` (`pipx install poetry`). To create a new project environment with dependencies, do `poetry install` after cloning. Run tests with `poetry pytest`, open an interactive python session to test using `poetry run ipython`, run tests on all supported Python versions with `poetry run tox -p`, or jump into the environment directly with `poetry shell`.

Additionally, to keep code well-formatted when shared, install the `black` pre-commit hook (once) via: `poetry run pre-commit install`.

