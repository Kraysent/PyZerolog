from abc import ABC, abstractmethod
import json
from typing import Optional


class Formatter(ABC):
    @abstractmethod
    def format(self, data: dict) -> str:
        pass


class JSONFormatter(Formatter):
    def __init__(self, indent: Optional[int] = None, sort_keys: bool = True):
        self.indent = indent
        self.sort_keys = sort_keys

    def format(self, data: dict) -> str:
        return json.dumps(data, sort_keys=True, indent=self.indent)
