from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConvoreMailChannel")


@_attrs_define
class ConvoreMailChannel:
    """The specific convore mail channel information

    Attributes:
        sender_name (str): The default name of the sender. Can be overriden on a per-message basis. Example: John Smith.
        address (str): It should consist only of lowercase alphanumeric characters (a-z, 0-9), include at least 5
            digits, and end with '@convoremail.com' or '@convoreapplication.com'. Additionally, aliases are supported by
            appending '+alias' to the local part of the email address. For instance, 'foobar@convoremail.com' can have an
            alias like 'foobar+1@convoremail.com'. Emails sent to an alias are routed to the primary mailbox. Example:
            johnsmith@convoremail.com.
    """

    sender_name: str
    address: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sender_name = self.sender_name

        address = self.address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sender_name": sender_name,
                "address": address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sender_name = d.pop("sender_name")

        address = d.pop("address")

        convore_mail_channel = cls(
            sender_name=sender_name,
            address=address,
        )

        convore_mail_channel.additional_properties = d
        return convore_mail_channel

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
