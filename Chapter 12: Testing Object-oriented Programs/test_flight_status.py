from flight_status_redis import FlightStatusTracker
from unittest.mock import Mock, patch
import datetime
import pytest


@pytest.fixture
def tracker():
    return FlightStatusTracker()


def test_mock_method(tracker):
    tracker.redis.set = Mock()
    with pytest.raises(ValueError) as ex:
        tracker.change_status("AC101", "lost")
    assert ex.value.args[0] == "LOST is not a valid status"
    assert tracker.redis.set.call_count == 0


def test_patch(tracker):
    tracker.redis.set = Mock()
    fake_now = datetime.datetime(2015, 4, 1)
    with patch("datetime.datetime") as dt:
        dt.now.return_value = fake_now
        tracker.change_status("AC102", "on time")
    dt.now.assert_called_once_with()
    tracker.redis.set.assert_called_once_with(
        "flightno:AC102", "2015-04-01T00:00:00|ON TIME"
    )

