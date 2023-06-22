from enum import Enum


class RegExEnum(Enum):
    BRAND = (
        r'^[A-Z][a-zA-Z\d]{1,24}$',
        'First letter uppercase min 2 max 25 ch'
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
