import unittest

from zlog import (
    IntField,
    FloatField,
    MeasuredFloatField,
    StringField,
    BoolField,
    ListField,
    ExceptionField,
    DictField,
)


class TestFields(unittest.TestCase):
    def test_int(self):
        actual = IntField(5).log()
        expected = 5
        self.assertEqual(expected, actual)

    def test_float(self):
        actual = FloatField(5.5).log()
        expected = 5.5
        self.assertEqual(expected, actual)

    def test_measured_float(self):
        actual = MeasuredFloatField(5.5, "s").log()
        expected = "5.5 s"
        self.assertEqual(expected, actual)

    def test_string(self):
        actual = StringField("test").log()
        expected = "test"
        self.assertEqual(expected, actual)

    def test_bool(self):
        actual = BoolField(False).log()
        expected = False
        self.assertEqual(expected, actual)

    def test_list(self):
        actual = ListField([1, 2, 3, 4]).log()
        expected = [1, 2, 3, 4]
        self.assertEqual(expected, actual)

    def test_exception(self):
        actual = ExceptionField(RuntimeError("test")).log()
        expected = {"message": "test", "error": "RuntimeError"}
        self.assertDictEqual(expected, actual)

    def test_dict(self):
        actual = DictField({"test": "value", "int": 5}).log()
        expected = {"test": "value", "int": 5}
        self.assertDictEqual(expected, actual)
