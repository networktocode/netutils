# Release Checklist

This document is intended for library maintainers and outlines the steps to perform when releasing a new version of the library.

!!! important
    Before starting, make sure your **local** `develop`, `main` are all up to date with upstream!

    ```
    git fetch
    git switch develop && git pull
    ```

Choose your own adventure:

- Patch release from `develop`? Jump [here](#all-releases-from-develop).
- Minor release? Continue with [Minor Version Bumps](#minor-version-bumps) and then [All Releases from `develop`](#all-releases-from-develop).

## Minor Version Bumps

### Update Requirements

Every minor version release should refresh `poetry.lock`, so that it lists the most recent stable release of each package. To do this:

0. Run `poetry update --dry-run` to have Poetry automatically tell you what package updates are available and the versions it would upgrade to. This requires an existing environment created from the lock file (i.e. via `poetry install`).
1. Review each requirement's release notes for any breaking or otherwise noteworthy changes.
2. Run `poetry update <package>` to update the package versions in `poetry.lock` as appropriate.
3. If a required package requires updating to a new release not covered in the version constraints for a package as defined in `pyproject.toml`, (e.g. `Django ~3.1.7` would never install `Django >=4.0.0`), update it manually in `pyproject.toml`.
4. Run `poetry install` to install the refreshed versions of all required packages.
5. Run all tests (`poetry run invoke tests`) and check that the UI and API function as expected.

### Update Documentation

If there are any changes to the compatibility matrix (such as a bump in the minimum supported Nautobot version), update it accordingly.

Commit any resulting changes from the following sections to the documentation before proceeding with the release.

!!! tip
    Fire up the documentation server in your development environment with `poetry run mkdocs serve`! This allows you to view the documentation site locally (the link is in the output of the command) and automatically rebuilds it as you make changes.

### Verify the Installation and Upgrade Steps

Follow the [installation instructions](../admin/install.md) to perform a new production installation of the library. If possible, also test the [upgrade process](../admin/upgrade.md) from the previous released version.

The goal of this step is to walk through the entire install process *as documented* to make sure nothing there needs to be changed or updated, to catch any errors or omissions in the documentation, and to ensure that it is current with each release.

---

## All Releases from `develop`

### Verify CI Build Status

Ensure that continuous integration testing on the `develop` branch is completing successfully.

### Bump the Version

Update the package version using `poetry version` if necessary. This command shows the current version of the project or bumps the version of the project and writes the new version back to `pyproject.toml` if a valid bump rule is provided.

The new version must be a valid semver string or a valid bump rule: `patch`, `minor`, `major`, `prepatch`, `preminor`, `premajor`, `prerelease`. Always try to use a bump rule when you can.

Display the current version with no arguments:

```no-highlight
> poetry version
netutils 1.0.0-beta.2
```

Bump pre-release versions using `prerelease`:

```no-highlight
> poetry version prerelease
Bumping version from 1.0.0-beta.2 to 1.0.0-beta.3
```

For major versions, use `major`:

```no-highlight
> poetry version major
Bumping version from 1.0.0-beta.2 to 1.0.0
```

For patch versions, use `minor`:

```no-highlight
> poetry version minor
Bumping version from 1.0.0 to 1.1.0
```

And lastly, for patch versions, you guessed it, use `patch`:

```no-highlight
> poetry version patch
Bumping version from 1.1.0 to 1.1.1
```

Please see the [official Poetry documentation on `version`](https://python-poetry.org/docs/cli/#version) for more information.

### Update the Changelog

!!! important
    The changelog must adhere to the [Keep a Changelog](https://keepachangelog.com/) style guide.

This guide uses `1.4.2` as the new version in its examples, so change it to match the version you bumped to in the previous step! Every. single. time. you. copy/paste commands :)

First, create a release branch off of `develop` (`git switch -c release-1.4.2 develop`).

> You will need to have the project's poetry environment built at this stage, as the towncrier command runs **locally only**. If you don't have it, run `poetry install` first.
Generate release notes with `invoke generate-release-notes --version 1.4.2` and answer `yes` to the prompt `Is it okay if I remove those files? [Y/n]:`. This will update the release notes in `docs/admin/release_notes/version_X.Y.md`, stage that file in git, and `git rm` all the fragments that have now been incorporated into the release notes.

There are two possibilities:

1. If you're releasing a new major or minor version, rename the `version_X.Y.md` file accordingly (e.g. rename to `docs/admin/release_notes/version_1.4.md`). Update the `Release Overview` and add this new page to the table of contents within `mkdocs.yml`.
2. If you're releasing a patch version, copy your version's section from the `version_X.Y.md` file into the already existing `docs/admin/release_notes/version_1.4.md` file. Delete the `version_X.Y.md` file.

Stage all the changes (`git add`) and check the diffs to verify all of the changes are correct (`git diff --cached`).

Commit `git commit -m "Release v1.4.2"` and `git push` the staged changes.

### Submit Release Pull Request

Submit a pull request titled `Release v1.4.2` to merge your release branch into `main`. Copy the documented release notes into the pull request's body.

!!! important
    Do not squash merge this branch into `main`. Make sure to select `Create a merge commit` when merging in GitHub.

Once CI has completed on the PR, merge it.

### Create a New Release in GitHub

Draft a [new release](https://github.com/networktocode/netutils/releases/new) with the following parameters.

* **Tag:** Input current version (e.g. `v1.4.2`) and select `Create new tag: v1.4.2 on publish`
* **Target:** `main`
* **Title:** Version and date (e.g. `v1.4.2 - 2024-04-02`)

Click "Generate Release Notes" and edit the auto-generated content as follows:

- Change the entries generated by GitHub to only the usernames of the contributors. e.g. `* Updated dockerfile by @ntc_user in https://github.com/networktocode/netutils/pull/123` -> `* @ntc_user`.
    - This should give you the list for the new `Contributors` section.
    - Make sure there are no duplicated entries.
- Replace the content of the `What's Changed` section with the description of changes from the release PR (what towncrier generated).
- If it exists, leave the `New Contributors` list as it is.

The release notes should look as follows:

```markdown
## What's Changed

**Towncrier generated Changed/Fixed/Housekeeping etc. sections here**

## Contributors

* @alice
* @bob

## New Contributors

* @bob

**Full Changelog**: https://github.com/networktocode/netutils/compare/v1.4.1...v1.4.2
```

Publish the release!

### Create a PR from `main` back to `develop`

First, sync your `main` branch with upstream changes: `git switch main && git pull`.

Create a new branch from `main` called `release-1.4.2-to-develop` and use `poetry version prepatch` to bump the development version to the next release.

For example, if you just released `v1.4.2`:

```no-highlight
> git switch -c release-1.4.2-to-develop main
Switched to a new branch 'release-1.4.2-to-develop'
> poetry version prepatch
Bumping version from 1.4.2 to 1.4.3a1
> git add pyproject.toml && git commit -m "Bump version"
> git push
```

!!! important
    Do not squash merge this branch into `develop`. Make sure to select `Create a merge commit` when merging in GitHub.

Open a new PR from `release-1.4.2-to-develop` against `develop`, wait for CI to pass, and merge it.

### Final checks

At this stage, the CI should be running or finished for the `v1.4.2` tag and a package successfully published to PyPI and added into the GitHub Release. Double check that's the case.

Documentation should also have been built for the tag on ReadTheDocs and if you're reading this page online, refresh it and look for the new version in the little version fly-out menu down at the bottom right of the page.

All done!
