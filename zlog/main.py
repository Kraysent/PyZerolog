import enum
import json
import logging
import sys
import datetime
from typing import Any


class Level(enum.Enum):
    DEBUG = 10
    INFO = 20
    WARN = 30
    ERROR = 40
    FATAL = 50

    def to_string(self):
        d = {
            Level.DEBUG: "debug",
            Level.INFO: "info",
            Level.WARN: "warn",
            Level.ERROR: "error",
            Level.FATAL: "fatal",
        }
        return d.get(self, "info")


class LogEvent:
    def __init__(self, mode: Level, prettify: bool = False, enabled: bool = True):
        self.level = mode
        self.prettify = prettify
        self.enabled = enabled
        self.fields = {}

    def _add_custom_field(self, key: str, value: Any):
        if "fields" not in self.fields:
            self.fields["fields"] = {}

        self.fields["fields"][key] = value

    def string(self, key: str, value: str) -> "LogEvent":
        self._add_custom_field(key, value)
        return self

    def int(self, key: str, value: int) -> "LogEvent":
        self._add_custom_field(key, value)
        return self

    def float(self, key: str, value: float) -> "LogEvent":
        self._add_custom_field(key, value)
        return self

    def bool(self, key: str, value: bool) -> "LogEvent":
        self._add_custom_field(key, value)
        return self

    def send(self):
        if not self.enabled:
            return

        self.fields["level"] = self.level.to_string()
        self.fields["timestamp"] = datetime.datetime.now().isoformat()

        result = json.dumps(
            self.fields, sort_keys=True, indent=2 if self.prettify else None
        )

        match self.level:
            case Level.DEBUG:
                print(result)
            case Level.INFO:
                print(result)
            case Level.WARN:
                print(result)
            case Level.ERROR:
                print(result)
            case Level.FATAL:
                print(result)

    def msg(self, message: str):
        if not self.enabled:
            return

        if message != "":
            self.fields["message"] = message

        self.send()


class Logger:
    def __init__(self):
        self.prettify = False
        self.base_level = Level.INFO

    def _return_log_event(self, level: Level) -> LogEvent:
        return LogEvent(
            mode=level,
            prettify=self.prettify,
            enabled=level.value >= self.base_level.value,
        )

    def debug(self) -> LogEvent:
        return self._return_log_event(Level.DEBUG)

    def info(self) -> LogEvent:
        return self._return_log_event(Level.INFO)

    def warn(self) -> LogEvent:
        return self._return_log_event(Level.WARN)

    def error(self) -> LogEvent:
        return self._return_log_event(Level.ERROR)

    def fatal(self) -> LogEvent:
        return self._return_log_event(Level.FATAL)


logger = Logger()
