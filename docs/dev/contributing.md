# Contributing

Pull requests are welcomed and automatically built and tested against multiple versions of Python through GitHub Actions. 

Except for unit tests, testing is only supported on Python 3.13.

The project is packaged with a light development environment based on `Docker` to help with the local development of the project and to run tests within GitHub Actions.

The project is following Network to Code software development guidelines and is leveraging the following:

- Python linting and formatting: `pylint` and `ruff`.
- YAML linting is done with `yamllint`.
- Typing is done with `mypy`.

There are a number of things that are required in order to have a successful PR.

- All new functions must contain at least 1 example in their docstrings.
- Docstrings must conform to the google docstring [convention](https://google.github.io/styleguide/pyguide.html#381-docstrings).
- Unit test for newly added functions are required.
- If applicable, tests related to config parsing and compliance must be added.
- Update the jinja2 filter (netutils.utils.jinja2_convenience_function) for any new functions (see below for details).
- If you create a new file in the `netutils` folder, you must add a new file for including Python and update `mkdocs.yml` to include the addition (see below for details).
- Your PR must not introduce any required dependencies. You can introduce optional or development dependencies.

Documentation is built using [mkdocs](https://www.mkdocs.org/). The [Docker based development environment](dev_environment.md#docker-development-environment) can be started by running `invoke docs` [http://localhost:8001](http://localhost:8001) that auto-refreshes when you make any changes to your local files.

## Adding docs for a new python file

If adding a new python file, the docs must be updated to account for the new file.

1. Create a new markdown file in `docs/dev/code_reference` matching the name of your new file such as `dns.md`.
2. Apply the following pattern to the newly created file.
3. Update the `mydocs.yml` to point to the new file

```python
# DNS

::: netutils.dns
    options:
        show_submodules: True
```

Update the mkdocs as appropriate, as shown in this truncated example of adding DNS.

```yaml
nav:
  - Developer Guide:
      - Extending the Library: "dev/extending.md"
      - Contributing to the Library: "dev/contributing.md"
      - Development Environment: "dev/dev_environment.md"
      - Development Config: "dev/dev_config.md"
      - Code Attribution to the Library: "dev/attribution.md"
      - Code Reference:
          - "dev/code_reference/index.md"
          - ASN: "dev/code_reference/asn.md"
          - Bandwidth: "dev/code_reference/bandwidth.md"
          - Banner: "dev/code_reference/banner.md"
          - Configs: "dev/code_reference/configs.md"
          - DNS: "dev/code_reference/dns.md" <<-- Added
```

## Adding Lib Mapper, jinja2 filter, or Config Parser

When adding to any of these features, you must run the `development_scripts` from the root directory. This process requires having Jinja2 on the machine that will run the process. This is automatically tested via pytest.

## Adding to the jinja2 filter function

To add a new function to the jinja2 filter, add a new entry to the `_JINJA2_FUNCTION_MAPPINGS` located in the `utils.py` file. When adding an entry, the key corresponds with the name to call the function and the value to the path to find the function.


Documentation is built using [mkdocs](https://www.mkdocs.org/). The [Docker based development environment](dev_environment.md#docker-development-environment) can be started by running `invoke docs` [http://localhost:8001](http://localhost:8001) that auto-refreshes when you make any changes to your local files.

## Creating Changelog Fragments

All pull requests to `next` or `develop` must include a changelog fragment file in the `./changes` directory. To create a fragment, use your GitHub issue number and fragment type as the filename. For example, `2362.added`. Valid fragment types are `added`, `changed`, `deprecated`, `fixed`, `removed`, and `security`. The change summary is added to the file in plain text. Change summaries should be complete sentences, starting with a capital letter and ending with a period, and be in past tense. Each line of the change fragment will generate a single change entry in the release notes. Use multiple lines in the same file if your change needs to generate multiple release notes in the same category. If the change needs to create multiple entries in separate categories, create multiple files.

!!! example

    **Wrong**
    ```plaintext title="changes/1234.fixed"
    fix critical bug in documentation
    ```

    **Right**
    ```plaintext title="changes/1234.fixed"
    Fixed critical bug in documentation.
    ```

!!! example "Multiple Entry Example"

    This will generate 2 entries in the `fixed` category and one entry in the `changed` category.

    ```plaintext title="changes/1234.fixed"
    Fixed critical bug in documentation.
    Fixed release notes generation.
    ```

    ```plaintext title="changes/1234.changed"
    Changed release notes generation.
    ```

## Branching Policy

The branching policy includes the following tenets:

- The develop branch is the primary branch to develop off of.
- If there is a reason to have a patch version, the maintainers may use cherry-picking strategy.
- PRs intended to add new features should be sourced from the develop branch.
- PRs intended to address bug fixes and security patches should be sourced from the develop branch.
- PRs intended to add new features that break backward compatibility should be discussed before a PR is created.

<<<<<<< HEAD
Netutils will observe semantic versioning, as of 1.0. This may result in an quick turn around in minor versions to keep pace with an ever growing feature set.
=======
Netutils will observe Semantic Versioning, as of 1.0. This may result in an quick turn around in minor versions to keep pace with an ever growing feature set.
>>>>>>> f4d378c (Cookie updated by NetworkToCode Cookie Drift Manager Tool)

## Release Policy

Netutils has currently no intended scheduled release schedule, and will release new features in minor versions.

When a new release is created the following should happen.

- A release PR is created with:
    - Update to the changelog in `docs/admin/release_notes/version_<major>.<minor>.md` file to reflect the changes.
    - Change the version from `<major>.<minor>.<patch>-beta` to `<major>.<minor>.<patch>` in pyproject.toml.
    - Set the PR to the main
- Ensure the tests for the PR pass.
- Merge the PR.
- Create a new tag:
    - The tag should be in the form of `v<major>.<minor>.<patch>`.
    - The title should be in the form of `v<major>.<minor>.<patch>`.
    - The description should be the changes that were added to the `version_<major>.<minor>.md` document.
- If merged into `main`, then push from `main` to `develop`, in order to retain the merge commit created when the PR was merged
- A post release PR is created with.
    - Change the version from `<major>.<minor>.<patch>` to `<major>.<minor>.<patch + 1>-beta` pyproject.toml.
    - Set the PR to the `develop`.
    - Once tests pass, merge.
