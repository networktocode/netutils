from os import path

import yaml
import pytest


@pytest.fixture(scope="module")
def generated_config_junos():
    return open(f"{_fixture_dir()}/generated_config_junos.conf").read()


@pytest.fixture(scope="module")
def running_config_junos():
    return open(f"{_fixture_dir()}/running_config_junos.conf").read()


@pytest.fixture(scope="module")
def generated_config_flat_junos():
    return open(f"{_fixture_dir()}/generated_config_flat_junos.conf").read()


@pytest.fixture(scope="module")
def running_config_flat_junos():
    return open(f"{_fixture_dir()}/running_config_flat_junos.conf").read()


@pytest.fixture(scope="module")
def remediation_config_flat_junos():
    return open(f"{_fixture_dir()}/remediation_config_flat_junos.conf").read()


@pytest.fixture(scope="module")
def options_junos():
    return yaml.safe_load(open(f"{_fixture_dir()}/options_junos.yml").read())


@pytest.fixture(scope="module")
def generated_config():
    return open(f"{_fixture_dir()}/generated_config.conf").read()


@pytest.fixture(scope="module")
def running_config():
    return open(f"{_fixture_dir()}/running_config.conf").read()


@pytest.fixture(scope="module")
def remediation_config_with_safe_tags():
    return open(f"{_fixture_dir()}/remediation_config_with_safe_tags.conf").read()


@pytest.fixture(scope="module")
def remediation_config_without_tags():
    return open(f"{_fixture_dir()}/remediation_config_without_tags.conf").read()


@pytest.fixture(scope="module")
def options_ios():
    return yaml.safe_load(open(f"{_fixture_dir()}/options_ios.yml").read())


@pytest.fixture(scope="module")
def tags_ios():
    return yaml.safe_load(open(f"{_fixture_dir()}/tags_ios.yml").read())


@pytest.fixture(scope="module")
def options_negate_with_undo():
    return yaml.safe_load(open(f"{_fixture_dir()}/options_negate_with_undo.yml").read())


def _fixture_dir():
    return path.join(path.dirname(path.realpath(__file__)), "fixtures")
