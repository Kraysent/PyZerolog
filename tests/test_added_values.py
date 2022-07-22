import json
import unittest
from unittest import mock

from tests.root import DatetimeMock, mocked_dt_str
from zlog import logger


class TestCustomValues(unittest.TestCase):
    def sample_input(self) -> str:
        return "hello"

    def sample_result(self, level: str, pop: list[str] = None) -> str:
        pop = pop or []
        res = {
            "timestamp": mocked_dt_str,
            "level": level,
            "message": "hello",
            "fields": {},
        }

        for field in pop:
            res.pop(field)

        return res

    @mock.patch("zlog.main.logging")
    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_no_fields(self, logging_mock):
        logging_mock.debug = mock.Mock()
        logger.debug().send()

        expected = {"timestamp": mocked_dt_str, "level": "debug"}
        expected = json.dumps(expected, sort_keys=True)
        logging_mock.debug.assert_called_once_with(expected)

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

    @mock.patch("zlog.main.logging")
    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_string_and_int(self, logging_mock):
        logging_mock.debug = mock.Mock()
        logger.debug().string("test", "value").int("sample", 8).msg(self.sample_input())

        expected = self.sample_result("debug")
        expected["fields"]["test"] = "value"
        expected["fields"]["sample"] = 8
        expected = json.dumps(expected, sort_keys=True)
        logging_mock.debug.assert_called_once_with(expected)

    @mock.patch("zlog.main.logging")
    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_float_and_string(self, logging_mock):
        logging_mock.debug = mock.Mock()
        logger.debug().float("test", 4.5).string("sample", "123").msg(
            self.sample_input()
        )

        expected = self.sample_result("debug")
        expected["fields"]["test"] = 4.5
        expected["fields"]["sample"] = "123"
        expected = json.dumps(expected, sort_keys=True)
        logging_mock.debug.assert_called_once_with(expected)
