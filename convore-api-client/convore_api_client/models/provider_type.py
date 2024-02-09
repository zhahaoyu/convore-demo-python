from enum import Enum


class ProviderType(str, Enum):
    CONVORE_CHAT = "convore_chat"
    CONVORE_GMAIL = "convore_gmail"
    CONVORE_MAIL = "convore_mail"
    GMAIL = "gmail"
    SES = "ses"

    def __str__(self) -> str:
        return str(self.value)
