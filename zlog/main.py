import enum
import logging


class Mode(enum.Enum):
    DEBUG = 10
    INFO = 20
    WARN = 30
    ERROR = 40
    FATAL = 50


class LogEntry:
    def __init__(self, mode: Mode):
        self.mode = mode

    def msg(self, message: str):
        match self.mode:
            case Mode.DEBUG:
                logging.debug(message)
            case Mode.INFO:
                logging.info(message)
            case Mode.WARN:
                logging.warn(message)
            case Mode.ERROR:
                logging.error(message)
            case Mode.FATAL:
                logging.fatal(message)


class Logger:
    def debug(self) -> LogEntry:
        return LogEntry(mode=Mode.DEBUG)

    def info(self) -> LogEntry:
        return LogEntry(mode=Mode.INFO)

    def warn(self) -> LogEntry:
        return LogEntry(mode=Mode.WARN)

    def error(self) -> LogEntry:
        return LogEntry(mode=Mode.ERROR)

    def fatal(self) -> LogEntry:
        return LogEntry(mode=Mode.FATAL)


logger = Logger()
