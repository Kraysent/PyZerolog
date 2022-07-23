from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


class Field(ABC):
    @abstractmethod
    def log(self) -> dict[str, Any] | list[Any] | int | float | str:
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
class MeasuredFloatField(Field):
    value: float
    unit: str

    def log(self) -> str:
        return f"{self.value} {self.unit}"


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


@dataclass
class ListField(Field):
    value: list[Any]

    def log(self) -> list[Any]:
        return self.value


@dataclass
class DictField(Field):
    value: dict[str, Any]

    def log(self) -> dict[str, Any]:
        return self.value


@dataclass
class ExceptionField(Field):
    value: Exception

    def log(self) -> dict[str, str]:
        return {"message": str(self.value), "error": type(self.value).__name__}
