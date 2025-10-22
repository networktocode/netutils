"""Example cli using click."""

import logging

import click

from netutils.log import initialize_logging

# Import necessary project related things to use in CLI

log = logging.getLogger(__name__)


@click.command()
@click.option("--test", default="Test Output", help="Test argument")
@click.option(
    "--log-level",
    default="INFO",
    type=click.Choice(["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]),
    help="Logging level",
)
@click.option("--log-file", default=None, help="Log file to output to debug logs to.")
def main(test, log_level, log_file):
    """Entrypoint into CLI app."""
    initialize_logging(level=log_level, filename=log_file)
    log.info("Entrypoint of the CLI app.")
    print(test)
