import unittest

from zlog import JSONFormatter


class TestJSONFormatter(unittest.TestCase):
    def test_empty(self):
        formatter = JSONFormatter()
        actual = formatter.format({})
        expected = "{}"
        self.assertEqual(expected, actual)

    def test_one_entry(self):
        formatter = JSONFormatter()
        actual = formatter.format({"test_key": "test value"})
        expected = '{"test_key": "test value"}'
        self.assertEqual(expected, actual)

    def test_two_entries(self):
        formatter = JSONFormatter()
        actual = formatter.format(
            {"test_key1": "test value 1", "test_key2": "test value 2"}
        )
        expected = '{"test_key1": "test value 1", "test_key2": "test value 2"}'
        self.assertEqual(expected, actual)

    def test_pretty(self):
        formatter = JSONFormatter(indent=2)
        actual = formatter.format(
            {"test_key1": "test value 1", "test_key2": "test value 2"}
        )
        expected = '''{
  "test_key1": "test value 1",
  "test_key2": "test value 2"
}'''
        self.assertEqual(expected, actual)
