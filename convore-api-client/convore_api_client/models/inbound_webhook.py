from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inbound_webhook_status import InboundWebhookStatus
from ..models.inbound_webhook_type import InboundWebhookType

T = TypeVar("T", bound="InboundWebhook")


@_attrs_define
class InboundWebhook:
    """The inbound webhook that this connector is associated with

    Attributes:
        type (InboundWebhookType):
        status (InboundWebhookStatus):
        url (str):
    """

    type: InboundWebhookType
    status: InboundWebhookStatus
    url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        status = self.status.value

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "status": status,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = InboundWebhookType(d.pop("type"))

        status = InboundWebhookStatus(d.pop("status"))

        url = d.pop("url")

        inbound_webhook = cls(
            type=type,
            status=status,
            url=url,
        )

        inbound_webhook.additional_properties = d
        return inbound_webhook

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
