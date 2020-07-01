# Software Engineering Hygiene for Machine Learning & Data Science

All production-ready machine learning code should read and feel no different from
any other high-quality codebase. The principles of reliable builds, testable
code, straightforward and distilled interfaces,and clearly documented design
decisions vastly improve the ease-of-use and maintenance of any code.


### Minimum for Personal and Small-Team Use
At a minmum, _any_ machine learning or otherwise data-interacting code should have the following in its `git` repository:

1. A descriptive, Markdown-formatted **`README.md`** that explains what the [code does and its purpose](
https://www.makeareadme.com/).
2. [Python **docstrings**](https://www.python.org/dev/peps/pep-0257/) for the most important classes, modules, and public functions. 
3. A simple, repeatable process for **environment** creation (e.g. a [`conda create`](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). and [`pip install -r`](https://pip.pypa.io/en/stable/reference/pip_install/)).
4. **tests** on core functionality (i.e. meaningful) that can be reliably executed (i.e. [`pytest`](https://docs.pytest.org/en/latest/contents.html)).
5. The `main` branch in a **clean, working state** at all times. Feature branches are where development should occur, including exploring breaking changes.
6. The **commit history** on `main` should be [clean](https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/best-practices), clear, and descriptive. Intermediate commits should never be merged into the main code branch.
7. Have **continuous integration (CI)** setup. The [GitLab CI](https://docs.gitlab.com/ee/ci/) job _should fail_ if _any code fails to build_ or if _any dependency fails to download_ or if _any test fails to pass_.



### Production-Quality Code
Additionally, production-quality machine learning code (i.e. it's making money and you have to deal with it everyday) should strive for further exacting commitments to quality and reliablity. In particular, it is a good idea to adopt:

8. code formatting using [`black`](https://github.com/ambv/black) and [`git` hooks](https://githooks.com/).
9. Actively use [`coverage`](https://coverage.readthedocs.io/) to inspect test code coverage to keep the coverage percentage as _high as possible_.
10. 100% code coverage via  unit tests.
12. Documentation on every function, class, and module.
13. Documentation building using [`sphinx`](http://www.sphinx-doc.org/en/stable/) or another community-supported documentation standard.
14. Prose-style documentation further describing the project's function and how different components interact with one another. Clear, direct technical writing documenting the project's intent, the data situation, the business impact and importance, as well as how the code architecture is designed is incredibly useful information for onboarding new scientists and engineeers.
15. If the modeling work is ultimately going into a deployed service (i.e. a REST model inference server), then ensure that the deployed model code has an [integration test](https://en.wikipedia.org/wiki/Integration_testing) that works both locally (via [`docker run`](https://docs.docker.com/engine/reference/run/)) and on the production platform (e.g. a [`kubernetes (k8s) cluster`](https://kubernetes.io/)).
16. Add an automation workflow where versions of `main`-line code, model configurations, and learned model artifacts are able to be deployed with a single command.
17. Hook-up this automation workflow to a release process, such as adding a `git tag` and having a CI tool initiate, where you may push to production. Ensure that there exists a roll-back mechanism as well (e.g. `kubectl rollout undo`).
18. Incorporate ETL and model training automation to a single-command process to take new, fresh data and determine if the production models should be updated.

The final recommendation is to adopt a coding style or philosophy as a living document concept. Evovle the notion adhereing to a "coding style document" into a shared ethos of the team: it is the common thought-language people approach writing programs in a small group of data nerds.
