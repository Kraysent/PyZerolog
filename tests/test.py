import unittest
import unittest.mock as mock
from zlog import logger


class TestBaseModes(unittest.TestCase):
    @mock.patch("zlog.main.logging")
    def test_debug_msg(self, logging_mock):
        logging_mock.debug = mock.Mock()
        logger.debug().msg("hello")
        logging_mock.debug.assert_called_once_with("hello")

    @mock.patch("zlog.main.logging")
    def test_info_msg(self, logging_mock):
        logging_mock.info = mock.Mock()
        logger.info().msg("hello")
        logging_mock.info.assert_called_once_with("hello")

    @mock.patch("zlog.main.logging")
    def test_warn_msg(self, logging_mock):
        logging_mock.warn = mock.Mock()
        logger.warn().msg("hello")
        logging_mock.warn.assert_called_once_with("hello")

    @mock.patch("zlog.main.logging")
    def test_error_msg(self, logging_mock):
        logging_mock.error = mock.Mock()
        logger.error().msg("hello")
        logging_mock.error.assert_called_once_with("hello")

    @mock.patch("zlog.main.logging")
    def test_fatal_msg(self, logging_mock):
        logging_mock.fatal = mock.Mock()
        logger.fatal().msg("hello")
        logging_mock.fatal.assert_called_once_with("hello")
