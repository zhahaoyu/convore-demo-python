from enum import Enum


class AuthorizationFlowStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    USED = "used"

    def __str__(self) -> str:
        return str(self.value)
