from unittest.mock import Mock
from lib.Time_Error import *

def test_difference_between_local_and_remote():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime": 1668262850}
    timer_mock = Mock()
    timer_mock.time.return_value = 1668262850.5
    time_error = TimeError(requester_mock, timer_mock)
    assert time_error.error() == -0.5