import io
import json
import unittest
import unittest.mock as mock
from tests.root import DatetimeMock
from zlog import logger


class TestBaseModes(unittest.TestCase):
    def setUp(self):
        self.output_stream = io.StringIO()
        logger.formatted_streams[0].stream = self.output_stream

    def sample_input(self) -> str:
        return "hello"

    def sample_result(self, level: str) -> str:
        dump = json.dumps(
            {
                "message": "hello",
                "level": level,
                "timestamp": "2001-01-01T12:00:00",
            },
            sort_keys=True,
        )
        dump = f"{dump}\n"
        return dump

    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_debug_msg(self):
        logger.debug().msg(self.sample_input())
        self.assertEqual(self.output_stream.getvalue(), "")

    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_info_msg(self):
        logger.info().msg(self.sample_input())
        self.assertEqual(self.output_stream.getvalue(), self.sample_result("info"))

    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_warn_msg(self):
        logger.warn().msg(self.sample_input())
        self.assertEqual(self.output_stream.getvalue(), self.sample_result("warn"))

    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_error_msg(self):
        logger.error().msg(self.sample_input())
        self.assertEqual(self.output_stream.getvalue(), self.sample_result("error"))

    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_fatal_msg(self):
        logger.fatal().msg(self.sample_input())
        self.assertEqual(self.output_stream.getvalue(), self.sample_result("fatal"))
