import enum
import json
import logging
import sys
import datetime
from typing import Any


class Level(enum.Enum):
    DEBUG = "debug"
    INFO = "info"
    WARN = "warn"
    ERROR = "error"
    FATAL = "fatal"


class LogEntry:
    def __init__(self, mode: Level):
        self.level = mode
        self.fields = {}

    def _add_custom_field(self, key: str, value: Any):
        if "fields" not in self.fields:
            self.fields["fields"] = {}

        self.fields["fields"][key] = value

    def string(self, key: str, value: str) -> "LogEntry":
        self._add_custom_field(key, value)
        return self

    def int(self, key: str, value: int) -> "LogEntry":
        self._add_custom_field(key, value)
        return self

    def float(self, key: str, value: float) -> "LogEntry":
        self._add_custom_field(key, value)
        return self

    def send(self):
        self.fields["level"] = self.level.value
        self.fields["timestamp"] = datetime.datetime.now().isoformat()

        result = json.dumps(self.fields, sort_keys=True)

        match self.level:
            case Level.DEBUG:
                logging.debug(result)
            case Level.INFO:
                logging.info(result)
            case Level.WARN:
                logging.warn(result)
            case Level.ERROR:
                logging.error(result)
            case Level.FATAL:
                logging.fatal(result)

    def msg(self, message: str):
        if message != "":
            self.fields["message"] = message

        self.send()


class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format="%(message)s")
        logging.StreamHandler(sys.stderr)

    def debug(self) -> LogEntry:
        return LogEntry(mode=Level.DEBUG)

    def info(self) -> LogEntry:
        return LogEntry(mode=Level.INFO)

    def warn(self) -> LogEntry:
        return LogEntry(mode=Level.WARN)

    def error(self) -> LogEntry:
        return LogEntry(mode=Level.ERROR)

    def fatal(self) -> LogEntry:
        return LogEntry(mode=Level.FATAL)


logger = Logger()
