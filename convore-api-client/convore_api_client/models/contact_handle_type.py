from enum import Enum


class ContactHandleType(str, Enum):
    CONVORE_CHAT = "convore_chat"
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
