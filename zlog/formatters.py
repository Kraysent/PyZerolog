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


class ConsoleFormatter(Formatter):
    def format(self, data: dict) -> str:
        result = ""

        time = data.get("timestamp", datetime.datetime.now())
        result += f"{time.hour:02d}:{time.minute:02d}"

        level_str = data.get("level", Level.INFO).to_short_string().upper()
        result += f" {level_str}"

        msg = data.get("message", "")
        if msg != "":
            result += f" {msg}"

        fields = [f"{key}={value}" for key, value in data.get("fields", {}).items()]
        if fields != []:
            result += f" {' '.join(fields)}"

        return result
