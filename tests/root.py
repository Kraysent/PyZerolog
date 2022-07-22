from datetime import datetime

mocked_dt_str = "2001-01-01T12:00:00"


class DatetimeMock:
    @classmethod
    def now(cls) -> "DatetimeMock":
        return datetime(2001, 1, 1, 12, 0, 0)

    def isoformat(self) -> str:
        return mocked_dt_str
