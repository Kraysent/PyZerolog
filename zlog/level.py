import enum


class Level(enum.Enum):
    DEBUG = 10
    INFO = 20
    WARN = 30
    ERROR = 40
    FATAL = 50

    def to_string(self):
        return {
            Level.DEBUG: "debug",
            Level.INFO: "info",
            Level.WARN: "warn",
            Level.ERROR: "error",
            Level.FATAL: "fatal",
        }.get(self, "info")

    def to_short_string(self):
        return {
            Level.DEBUG: "dbg",
            Level.INFO: "inf",
            Level.WARN: "wrn",
            Level.ERROR: "err",
            Level.FATAL: "ftl",
        }.get(self, "inf")
