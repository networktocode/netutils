# netutils

## Documentation

The documentation of each repo and its APIs can be found in the [netutils Page](https://https://networktocode-llc.github.io/netutils). It is created and published by Github actions every time you cut a new release, as long as all tests are passing. The action name is `pages` and can be found in `.github/workflows/ci.yml`.

### Requirements

If you want to build the documentation on a GitHub page:

1. Ensure that all tests are passing.

2. Follow the release and tagging process.

3. Go to the repository "Settings", then go to "Pages", and select the source branch: `ntc-pages`.

---
**NOTE**

The page url uses the repository name to formulate the url: `https://https://networktocode-llc.github.io/{ repo_name }`. For consistency, we recommend that the repository name should be the same as the project slug from the cookie cutter template: `https://https://networktocode-llc.github.io/netutils`

---


### Local Doc Build

If you want to build the documentation locally, follow these steps:

1. Run poetry to install all necessary packages: 

```bash
$ poetry install
$ poetry shell
```

2. Create local docs:

```bash
$ sphinx-build -vvv -b html ./docs public
``

3. Run a local python server to check your documentation rendering:

```bash
cd public
python -m http.server &
```


