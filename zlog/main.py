import enum
import datetime
import sys
from typing import IO
from zlog.fields import BoolField, Field, FloatField, IntField, StringField

from zlog.formatters import JSONFormatter


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
    def __init__(
        self,
        mode: Level,
        enabled: bool = True,
        output_stream: IO = sys.stdout,
        formatter=JSONFormatter(),
    ):
        self.level = mode
        self.enabled = enabled
        self.fields = {}
        self.output_stream = output_stream
        self.formatter = formatter

    def _add_custom_field(self, key: str, value: Field):
        if "fields" not in self.fields:
            self.fields["fields"] = {}

        self.fields["fields"][key] = value.log()

    def string(self, key: str, value: str) -> "LogEvent":
        self._add_custom_field(key, StringField(value))
        return self

    def int(self, key: str, value: int) -> "LogEvent":
        self._add_custom_field(key, IntField(value))
        return self

    def float(self, key: str, value: float) -> "LogEvent":
        self._add_custom_field(key, FloatField(value))
        return self

    def bool(self, key: str, value: bool) -> "LogEvent":
        self._add_custom_field(key, BoolField(value))
        return self

    def send(self):
        if not self.enabled:
            return

        self.fields["level"] = self.level.to_string()
        self.fields["timestamp"] = datetime.datetime.now().isoformat()

        result = self.formatter.format(self.fields)

        self.output_stream.write(result)
        self.output_stream.write("\n")

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
        self.output_stream = sys.stdout
        self.formatter = JSONFormatter(2 if self.prettify else None)

    def _return_log_event(self, level: Level) -> LogEvent:
        return LogEvent(
            mode=level,
            enabled=level.value >= self.base_level.value,
            output_stream=self.output_stream,
            formatter=self.formatter,
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
