from enum import Enum


class InboundWebhookStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"

    def __str__(self) -> str:
        return str(self.value)
