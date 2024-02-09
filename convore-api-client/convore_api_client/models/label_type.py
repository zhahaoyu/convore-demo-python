from enum import Enum


class LabelType(str, Enum):
    CHANNEL_PRIVATE = "channel_private"
    SHARED = "shared"

    def __str__(self) -> str:
        return str(self.value)
