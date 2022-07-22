import json
import unittest
from unittest import mock
from tests.root import DatetimeMock, mocked_dt_str

from zlog import Formatter, JSONFormatter


class TestJSONFormatter(unittest.TestCase):
    @mock.patch("zlog.formatters.datetime.datetime", new=DatetimeMock)
    def get_actual(self, formatter: Formatter, input: dict) -> str:
        return formatter.format(input)

    def test_empty(self):
        formatter = JSONFormatter()
        actual = self.get_actual(formatter, {})
        expected = json.dumps(
            {"timestamp": mocked_dt_str, "level": "info"}, sort_keys=True
        )
        self.assertEqual(expected, actual)

    def test_one_entry(self):
        formatter = JSONFormatter()
        actual = self.get_actual(formatter, {"test_key": "test value"})
        expected = json.dumps(
            {"timestamp": mocked_dt_str, "level": "info", "test_key": "test value"},
            sort_keys=True,
        )
        self.assertEqual(expected, actual)

    def test_two_entries(self):
        formatter = JSONFormatter()
        actual = self.get_actual(
            formatter, {"test_key1": "test value 1", "test_key2": "test value 2"}
        )
        expected = json.dumps(
            {
                "timestamp": mocked_dt_str,
                "level": "info",
                "test_key1": "test value 1",
                "test_key2": "test value 2",
            },
            sort_keys=True,
        )
        self.assertEqual(expected, actual)

    def test_pretty(self):
        formatter = JSONFormatter(indent=2)
        actual = self.get_actual(
            formatter, {"test_key1": "test value 1", "test_key2": "test value 2"}
        )
        expected = json.dumps(
            {
                "timestamp": mocked_dt_str,
                "level": "info",
                "test_key1": "test value 1",
                "test_key2": "test value 2",
            },
            sort_keys=True,
            indent=2,
        )
        self.assertEqual(expected, actual)
