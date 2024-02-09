from enum import Enum


class MessageFormat(str, Enum):
    FULL = "full"
    MINIMAL = "minimal"

    def __str__(self) -> str:
        return str(self.value)
