from enum import Enum


class ConversationStatus(str, Enum):
    DONE = "done"
    OPEN = "open"
    SPAM = "spam"
    TRASH = "trash"

    def __str__(self) -> str:
        return str(self.value)
