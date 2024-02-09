from enum import Enum


class ConversationPriority(str, Enum):
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"
    NO_PRIORITY = "no_priority"
    URGENT = "urgent"

    def __str__(self) -> str:
        return str(self.value)
