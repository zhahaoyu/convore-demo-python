from enum import Enum


class ObjectType(str, Enum):
    CONVERSATION = "conversation"
    LABEL = "label"
    MESSAGE = "message"

    def __str__(self) -> str:
        return str(self.value)
