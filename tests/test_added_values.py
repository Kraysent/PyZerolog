import io
import json
import sys
import unittest
from unittest import mock

from tests.root import DatetimeMock, mocked_dt_str
from zlog import logger


class TestCustomValues(unittest.TestCase):
    def setUp(self):
        output_stream = io.StringIO()
        logger.output_stream = output_stream
        self.output_stream = output_stream

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

    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_no_fields(self):
        logger.info().send()

        expected = {"timestamp": mocked_dt_str, "level": "info"}
        expected = f"{json.dumps(expected, sort_keys=True)}\n"
        self.assertEqual(self.output_stream.getvalue(), expected)

    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_string(self):
        logger.info().string("test", "value").msg(self.sample_input())

        expected = self.sample_result("info")
        expected["fields"]["test"] = "value"
        expected = f"{json.dumps(expected, sort_keys=True)}\n"
        self.assertEqual(self.output_stream.getvalue(), expected)

    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_int(self):
        logger.info().int("test", 5).msg(self.sample_input())

        expected = self.sample_result("info")
        expected["fields"]["test"] = 5
        expected = f"{json.dumps(expected, sort_keys=True)}\n"
        self.assertEqual(self.output_stream.getvalue(), expected)

    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_float(self):
        logger.info().string("test", 5.2).msg(self.sample_input())

        expected = self.sample_result("info")
        expected["fields"]["test"] = 5.2
        expected = f"{json.dumps(expected, sort_keys=True)}\n"
        self.assertEqual(self.output_stream.getvalue(), expected)

    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_bool(self):
        logger.info().bool("test", True).msg(self.sample_input())

        expected = self.sample_result("info")
        expected["fields"]["test"] = True
        expected = f"{json.dumps(expected, sort_keys=True)}\n"
        self.assertEqual(self.output_stream.getvalue(), expected)

    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_string_and_int(self):
        logger.info().string("test", "value").int("sample", 8).msg(self.sample_input())

        expected = self.sample_result("info")
        expected["fields"]["test"] = "value"
        expected["fields"]["sample"] = 8
        expected = f"{json.dumps(expected, sort_keys=True)}\n"
        self.assertEqual(self.output_stream.getvalue(), expected)

    @mock.patch("zlog.main.datetime.datetime", new=DatetimeMock)
    def test_float_and_string(self):
        logger.info().float("test", 4.5).string("sample", "123").msg(
            self.sample_input()
        )

        expected = self.sample_result("info")
        expected["fields"]["test"] = 4.5
        expected["fields"]["sample"] = "123"
        expected = f"{json.dumps(expected, sort_keys=True)}\n"
        self.assertEqual(self.output_stream.getvalue(), expected)
