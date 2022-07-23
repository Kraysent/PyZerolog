import datetime
import sys
from typing import IO
from zlog.fields import (
    BoolField,
    ExceptionField,
    Field,
    FloatField,
    IntField,
    ListField,
    StringField,
)
from zlog.formatters import Formatter, JSONFormatter
from zlog.level import Level


class FormattedStream:
    def __init__(self, formatter: Formatter = JSONFormatter(), stream: IO = sys.stdout):
        self.formatter = formatter
        self.stream = stream

    def format(self, data: dict) -> str:
        return self.formatter.format(data)

    def write(self, value: str):
        self.stream.write(value)


class LogEvent:
    def __init__(self, mode: Level, enabled: bool = True, formatted_streams=None):
        if formatted_streams is None:
            formatted_streams = [FormattedStream()]
        self.level = mode
        self.enabled = enabled
        self.fields = {}
        self.formatted_streams = formatted_streams

    def field(self, key: str, value: Field) -> "LogEvent":
        if "fields" not in self.fields:
            self.fields["fields"] = {}

        self.fields["fields"][key] = value.log()
        return self

    def string(self, key: str, value: str) -> "LogEvent":
        return self.field(key, StringField(value))

    def int(self, key: str, value: int) -> "LogEvent":
        return self.field(key, IntField(value))

    def float(self, key: str, value: float) -> "LogEvent":
        return self.field(key, FloatField(value))

    def bool(self, key: str, value: bool) -> "LogEvent":
        return self.field(key, BoolField(value))

    def list(self, key: str, value: list) -> "LogEvent":
        return self.field(key, ListField(value))

    def exception(self, key: str, value: Exception) -> "LogEvent":
        return self.field(key, ExceptionField(value))

    def send(self):
        if not self.enabled:
            return

        self.fields["level"] = self.level
        self.fields["timestamp"] = datetime.datetime.now()

        for formatted_stream in self.formatted_streams:
            result = formatted_stream.format(self.fields)
            formatted_stream.write(result)
            formatted_stream.write("\n")

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
        self.formatted_streams = [
            FormattedStream(JSONFormatter(2 if self.prettify else None), sys.stdout)
        ]

    def _return_log_event(self, level: Level) -> LogEvent:
        return LogEvent(
            mode=level,
            enabled=level.value >= self.base_level.value,
            formatted_streams=self.formatted_streams,
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
