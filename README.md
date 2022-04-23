- [About](#about)
- [Requirements on any tool like pre-commit](#requirements-on-any-tool-like-pre-commit)
- [Open questions to pre-commit](#open-questions-to-pre-commit)
- [Benefits of pre-commit](#benefits-of-pre-commit)
- [Sidenotes:](#sidenotes)
  - [How to install latest nodejs version in ubuntu](#how-to-install-latest-nodejs-version-in-ubuntu)

# About

Small prototype testing out the [pre-commit package](https://pre-commit.com/).

# Requirements on any tool like pre-commit

- one command to run all checks in CI and locally
  - with invoke:
    - CI: invoke lint
    - locally: invoke lint -o
  - with precommit
    - CI: pre-commit run --all-files
    - locally: pre-commit run (maybe with `git add .` beforehand to also run on unchanged files?!)
- Quickly add other python scripts
  - rather easy to do, simply add one file or function

Alternatives to pre-commit

Literature

- https://prettier.io/docs/en/precommit.html
- https://dev.to/krzysztofkaczy9/do-you-really-need-husky-24

- pre-commit, 8k stars
- husky
  - 30k stars
  - npm, so javascript based :/
- lint-staged
  - https://github.com/okonet/lint-staged
  - 10k stars
  - again npx, js based :/
- git-hooks

- https://github.com/andreoliwa/nitpick
  - from https://wemake-python-stylegui.de/en/latest/#:~:text=Welcome%20to%20the%20strictest%20and,some%20other%20plugins%20as%20dependencies.
  - also [recommends pre-commit](https://github.com/andreoliwa/nitpick#run-as-a-pre-commit-hook)

# Open questions to pre-commit

- does it work during rebase?
  - seems not, would need to add ["--exec" to the rebase](https://stackoverflow.com/a/70568833/2135504)
  - however, [pre-commit seems to run during merge-conflicts](https://pre-commit.com/#pre-commit-during-merges) and even in an intelligent way
- ## what exactly is system? (=python from venv?)
- can it also run on unstaged changes?
  - why would it? simply run `git add . && pre-commit run"
  - By default, it runs only on staged files, see run.py:L261
    - `git diff --staged`
  - Even `get_all_files` only runs on `git ls-files`, not on everything in repository
- why is stashing necessary?!
  - I guess pre-commit focuses on checking the staged files, not any other modifications. Because only staged files will be commited
  - However, if that is true, any other modifications need to be stashed away.
- can pre-commit run scripts both in Windows AND unix?!
  - hmm.. not sure. It simply seems to run the file as e.g. `<repo-dir>/my-executable`
  - Alternatively, we could probably

# Benefits of pre-commit

- Lots of specification for each hook
  - args
  - files to include / exclude
  - regex pattern
  - fail fast
- runs..
  - locally on modified files
  - on all files compared to e.g. master
  - on all files in CI
  - in pre-commit
- applies each hook on files in parallel -> quick
- easy to setup and use
- well tested and stable
- installs e.g. npm automatically (requires node though)
- allows to test new checks quickly via e.g. [try-repo](https://pre-commit.com/#developing-hooks-interactively)
  - see e.g https://github.com/pre-commit/pre-commit-hooks/blob/main/pre_commit_hooks/check_yaml.py

# Sidenotes:

## How to install latest nodejs version in ubuntu

https://github.com/nodesource/distributions/blob/master/README.md
