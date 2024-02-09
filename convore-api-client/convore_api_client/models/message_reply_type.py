from enum import Enum


class MessageReplyType(str, Enum):
    FORWARD = "forward"
    REPLY = "reply"
    REPLY_ALL = "reply_all"

    def __str__(self) -> str:
        return str(self.value)
