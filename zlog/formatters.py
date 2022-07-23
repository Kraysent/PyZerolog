from abc import ABC, abstractmethod
import datetime
import json
from typing import Optional
from zlog.level import Level


class Formatter(ABC):
    @abstractmethod
    def format(self, data: dict) -> str:
        pass


class JSONFormatter(Formatter):
    def __init__(self, indent: Optional[int] = None, sort_keys: bool = True):
        self.indent = indent
        self.sort_keys = sort_keys

    def format(self, data: dict) -> str:
        data["timestamp"] = data.get("timestamp", datetime.datetime.now()).isoformat()
        data["level"] = data.get("level", Level.INFO).to_string()
        return json.dumps(data, sort_keys=True, indent=self.indent)


class Color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

    @staticmethod
    def apply(string: str, color: "Color") -> str:
        return color + string + Color.END


class ConsoleFormatter(Formatter):
    def __init__(self, coloring: bool = True) -> None:
        self.coloring = coloring

    def format(self, data: dict) -> str:
        result = ""

        time = data.get("timestamp", datetime.datetime.now())
        if self.coloring:
            result += Color.apply(f"{time.hour:02d}:{time.minute:02d}", Color.YELLOW)
        else:
            result += f"{time.hour:02d}:{time.minute:02d}"

        level = data.get("level", Level.INFO)
        if self.coloring:
            color = {
                Level.DEBUG: Color.DARKCYAN,
                Level.INFO: Color.GREEN,
                Level.WARN: Color.RED,
                Level.ERROR: Color.PURPLE,
                Level.FATAL: Color.YELLOW,
            }.get(level, Color.GREEN)
            level = level.to_short_string().upper()
            result += Color.apply(f" {level}", color)
        else:
            result += f" {level.to_short_string().upper()}"

        msg = data.get("message", "")
        if msg != "":
            result += f" {msg} "

        if self.coloring:
            fields = [
                Color.apply(key, Color.YELLOW) + "=" + str(value)
                for key, value in data.get("fields", {}).items()
            ]
        else:
            fields = [
                key + "=" + str(value) for key, value in data.get("fields", {}).items()
            ]

        if fields != []:
            result += " ".join(fields)

        return result
