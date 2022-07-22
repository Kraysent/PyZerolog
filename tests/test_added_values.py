import json
import unittest
from unittest import mock

from tests.root import DatetimeMock
from zlog import logger


class TestCustomValues(unittest.TestCase):
    def sample_input(self) -> str:
        return "hello"

    def sample_result(self, level: str) -> str:
        return {
                "timestamp": "2001-01-01T12:00:00",
                "level": level,
                "message": "hello",
                "fields": {},
            }

    @mock.patch("zlog.main.logging")
    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_string(self, logging_mock):
        logging_mock.debug = mock.Mock()
        logger.debug().string("test", "value").msg(self.sample_input())

        expected = self.sample_result("debug")
        expected["fields"]["test"] = "value"
        expected = json.dumps(expected, sort_keys=True)
        logging_mock.debug.assert_called_once_with(expected)

    @mock.patch("zlog.main.logging")
    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_int(self, logging_mock):
        logging_mock.debug = mock.Mock()
        logger.debug().int("test", 5).msg(self.sample_input())

        expected = self.sample_result("debug")
        expected["fields"]["test"] = 5
        expected = json.dumps(expected, sort_keys=True)
        logging_mock.debug.assert_called_once_with(expected)

    @mock.patch("zlog.main.logging")
    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_float(self, logging_mock):
        logging_mock.debug = mock.Mock()
        logger.debug().string("test", 5.2).msg(self.sample_input())

        expected = self.sample_result("debug")
        expected["fields"]["test"] = 5.2
        expected = json.dumps(expected, sort_keys=True)
        logging_mock.debug.assert_called_once_with(expected)
