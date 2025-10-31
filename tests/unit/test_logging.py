"""Validate netutils logging works."""

import mock

import netutils


@mock.patch("logging.config.dictConfig")
@mock.patch("logging.getLogger")
def test_initialize_logging_default(get_logger, basic_cfg):
    """Test initialize_logging using defaults."""
    netutils.log.initialize_logging()

    basic_cfg.assert_called_once()
    initial_call = basic_cfg.mock_calls[0].args[0]
    assert set(initial_call.keys()) == set(
        ["version", "disable_existing_loggers", "formatters", "handlers", "loggers"]
    )
    assert initial_call["handlers"]["standard"]["level"] == "INFO"

    get_logger.assert_called_once()
    assert get_logger.mock_calls[0].args == ("netutils",)
    assert get_logger.mock_calls[1].args == ("Logging initialized.",)


@mock.patch("logging.config.dictConfig")
@mock.patch("logging.getLogger")
def test_initialize_logging_user_defined_config(get_logger, basic_cfg):
    """Test initialize_logging with user defined config."""
    config = {"version": 1, "disable_existing_loggers": False}
    netutils.log.initialize_logging(config=config)

    basic_cfg.assert_called_once()
    initial_call = basic_cfg.mock_calls[0].args[0]
    assert initial_call == config

    get_logger.assert_called_once()
    assert get_logger.mock_calls[0].args == ("netutils",)
    assert get_logger.mock_calls[1].args == ("Logging initialized.",)


@mock.patch("logging.config.dictConfig")
@mock.patch("logging.getLogger")
def test_initialize_logging_filename(get_logger, basic_cfg):
    """Test initialize_logging with filename."""
    netutils.log.initialize_logging(filename="output.log")

    basic_cfg.assert_called_once()
    initial_call = basic_cfg.mock_calls[0].args[0]
    assert set(initial_call.keys()) == set(
        ["version", "disable_existing_loggers", "formatters", "handlers", "loggers"]
    )
    assert initial_call["handlers"]["standard"]["level"] == "INFO"
    assert initial_call["handlers"]["file_output"]["filename"] == "output.log"
    assert initial_call["handlers"]["file_output"]["level"] == "DEBUG"
    assert initial_call["handlers"]["file_output"]["formatter"] == "debug"
    assert initial_call["handlers"]["file_output"]["class"] == "logging.FileHandler"
    assert "file_output" in initial_call["loggers"][""]["handlers"]

    get_logger.assert_called_once()
    assert get_logger.mock_calls[0].args == ("netutils",)
    assert get_logger.mock_calls[1].args == ("Logging initialized.",)
