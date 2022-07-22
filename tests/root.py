from datetime import datetime


class DatetimeMock:
    @classmethod
    def now(cls) -> 'DatetimeMock':
        return datetime(2001, 1, 1, 12, 0, 0)

    def isoformat(self) -> str:
        return "2001-01-01T12:00:00"