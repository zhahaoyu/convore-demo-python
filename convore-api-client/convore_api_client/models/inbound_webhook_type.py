from enum import Enum


class InboundWebhookType(str, Enum):
    SES_NOTIFICATION = "SES_NOTIFICATION"

    def __str__(self) -> str:
        return str(self.value)
