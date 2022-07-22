from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


class Field(ABC):
    @abstractmethod
    def log(self) -> dict[str, Any] | int | float | str:
        pass


@dataclass
class IntField(Field):
    value: int

    def log(self) -> int:
        return self.value


@dataclass
class FloatField(Field):
    value: float

    def log(self) -> float:
        return self.value


@dataclass
class StringField(Field):
    value: str

    def log(self) -> str:
        return self.value


@dataclass
class BoolField(Field):
    value: bool

    def log(self) -> bool:
        return self.value
