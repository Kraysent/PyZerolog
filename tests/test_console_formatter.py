import unittest
from unittest import mock

from tests.root import DatetimeMock
from zlog import Formatter, ConsoleFormatter


class TestConsoleFormatter(unittest.TestCase):
    @mock.patch("zlog.formatters.datetime.datetime", new=DatetimeMock)
    def get_actual(self, formatter: Formatter, input: dict) -> str:
        return formatter.format(input)

    def test_empty(self):
        formatter = ConsoleFormatter()
        actual = self.get_actual(formatter, {})
        expected = "12:00 INF"
        self.assertEqual(expected, actual)

    def test_one_entry(self):
        formatter = ConsoleFormatter()
        actual = self.get_actual(formatter, {"fields": {"test_key": "test value"}})
        expected = "12:00 INF test_key=test value"
        self.assertEqual(expected, actual)

    def test_two_entries(self):
        formatter = ConsoleFormatter()
        actual = self.get_actual(
            formatter,
            {"fields": {"test_key1": "test value 1", "test_key2": "test value 2"}},
        )
        expected = "12:00 INF test_key1=test value 1 test_key2=test value 2"
        self.assertEqual(expected, actual)
