import datetime
from unittest import mock
import sys
sys.path.append('../')
from to_test import time_of_day


@mock.patch('to_test.datetime')
def test_time_of_day_night(mock_date):
    mock_date.now.return_value = datetime.datetime(2021, 5, 21, 20, 0, 0)
    assert time_of_day() == 'night'


@mock.patch('to_test.datetime')
def test_time_of_day_morning(mock_date):
    mock_date.now.return_value = datetime.datetime(2021, 5, 21, 7, 0, 0)
    assert time_of_day() == 'morning'


@mock.patch('to_test.datetime')
def test_time_of_day_afternoon(mock_date):
    mock_date.now.return_value = datetime.datetime(2021, 5, 21, 15, 0, 0)
    assert time_of_day() == 'afternoon'
