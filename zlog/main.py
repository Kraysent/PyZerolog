import enum
import json
import logging
import sys
import datetime


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

    def msg(self, message: str):
        self.fields["message"] = message
        self.fields["level"] = self.level.value
        self.fields["timestamp"] = datetime.datetime.now().isoformat()
        result = json.dumps(self.fields)

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


class Logger:
    def __init__(self):
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
