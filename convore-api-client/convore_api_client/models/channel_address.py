from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_handle import ContactHandle


T = TypeVar("T", bound="ChannelAddress")


@_attrs_define
class ChannelAddress:
    """A collection of communication addresses associated with the channel. These addresses are used for sending and
    receiving messages, ensuring proper routing and delivery of content. Each address specifies a unique handle, such as
    an email or a phone number, along with associated details like the participant's name and role.

        Attributes:
            handle (ContactHandle): Handle of the contact. Can be any string used to uniquely identify the contact.
            name (Union[Unset, str]): Name of the sender. Example: John Doe.
            is_primary (Union[Unset, bool]): Whether the address is the primary address for the channel.
    """

    handle: "ContactHandle"
    name: Union[Unset, str] = UNSET
    is_primary: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        handle = self.handle.to_dict()

        name = self.name

        is_primary = self.is_primary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "handle": handle,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_handle import ContactHandle

        d = src_dict.copy()
        handle = ContactHandle.from_dict(d.pop("handle"))

        name = d.pop("name", UNSET)

        is_primary = d.pop("is_primary", UNSET)

        channel_address = cls(
            handle=handle,
            name=name,
            is_primary=is_primary,
        )

        channel_address.additional_properties = d
        return channel_address

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
