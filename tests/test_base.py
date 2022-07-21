from datetime import datetime
import json
import unittest
import unittest.mock as mock
from zlog import logger


class DatetimeMock:
    @classmethod
    def now(cls) -> 'DatetimeMock':
        return datetime(2001, 1, 1, 12, 0, 0)

    def isoformat(self) -> str:
        return "2001-01-01T12:00:00"

class TestBaseModes(unittest.TestCase):
    def sample_input(self):
        return "hello"

    def sample_result(self, level: str):
        return json.dumps(
            {"message": "hello", "level": level, "timestamp": "2001-01-01T12:00:00"}
        )

    @mock.patch("zlog.main.logging")
    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_debug_msg(self, logging_mock):
        logging_mock.debug = mock.Mock()
        logger.debug().msg(self.sample_input())
        logging_mock.debug.assert_called_once_with(self.sample_result("debug"))

    @mock.patch("zlog.main.logging")
    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_info_msg(self, logging_mock):
        logging_mock.info = mock.Mock()
        logger.info().msg(self.sample_input())
        logging_mock.info.assert_called_once_with(self.sample_result("info"))

    @mock.patch("zlog.main.logging")
    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_warn_msg(self, logging_mock):
        logging_mock.warn = mock.Mock()
        logger.warn().msg(self.sample_input())
        logging_mock.warn.assert_called_once_with(self.sample_result("warn"))

    @mock.patch("zlog.main.logging")
    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_error_msg(self, logging_mock):
        logging_mock.error = mock.Mock()
        logger.error().msg(self.sample_input())
        logging_mock.error.assert_called_once_with(self.sample_result("error"))

    @mock.patch("zlog.main.logging")
    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_fatal_msg(self, logging_mock):
        logging_mock.fatal = mock.Mock()
        logger.fatal().msg(self.sample_input())
        logging_mock.fatal.assert_called_once_with(self.sample_result("fatal"))
