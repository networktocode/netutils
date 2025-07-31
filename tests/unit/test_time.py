"""Test for the time functions."""

import pytest

from netutils.time import uptime_seconds_to_string, uptime_string_to_seconds

UPTIME_TO_STRING = [
    {
        "sent": 604800,
        "received": "1 week",
    },
    {
        "sent": 86400,
        "received": "1 day",
    },
    {
        "sent": 7200,
        "received": "2 hours",
    },
    {
        "sent": 3600,
        "received": "1 hour",
    },
    {
        "sent": 7250,
        "received": "2 hours, 50 seconds",
    },
    {
        "sent": 698490,
        "received": "1 week, 1 day, 2 hours, 1 minute, 30 seconds",
    },
    {
        "sent": 32148000,
        "received": "1 year, 1 week, 2 hours",
    },
]

UPTIME_TO_SECONDS = [
    {"sent": "1 week, 0 days, 0 hours, 10 minutes", "received": 605400},
    {"sent": "1 year, 11 minutes", "received": 31536660},
    {"sent": "58 minutes", "received": 3480},
    {"sent": "1 day, 15 hours, 10 minutes", "received": 141000},
    {"sent": "15:36:22", "received": 56182},
    {"sent": "2 days, 3:10:00", "received": 184200},
    {"sent": "4m15s", "received": 255},
    {"sent": "6d10m1s", "received": 519001},
    {"sent": "1y3w10m2s", "received": 33351002},
]


@pytest.mark.parametrize("data", UPTIME_TO_STRING)
def test_uptime_seconds_to_string(data):
    assert uptime_seconds_to_string(data["sent"]) == data["received"]


@pytest.mark.parametrize("data", UPTIME_TO_SECONDS)
def test_uptime_string_to_seconds(data):
    assert uptime_string_to_seconds(data["sent"]) == data["received"]


def test_fail_uptime_string_to_seconds():
    with pytest.raises(Exception, match=r"Unable to parse uptime string."):
        uptime_string_to_seconds("thisismytime")
