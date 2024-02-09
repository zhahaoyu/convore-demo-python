from enum import Enum


class MessageParticipantRole(str, Enum):
    BCC = "bcc"
    CC = "cc"
    FROM = "from"
    TO = "to"

    def __str__(self) -> str:
        return str(self.value)
