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

    def __init__(self, value: float, decimals: int | None = None):
        self.value = value
        self.decimals = decimals

    def log(self) -> float:
        if self.decimals is not None:
            return round(self.value, self.decimals)
        else:
            return self.value


@dataclass
class MeasuredFloatField(Field):
    value: float
    unit: str

    def __init__(self, value: float, unit: str, decimals: int | None = None):
        self.value = value
        self.unit = unit
        self.decimals = decimals

    def log(self) -> str:
        if self.decimals is not None:
            return f"{round(self.value, self.decimals)} {self.unit}"
        else:
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
