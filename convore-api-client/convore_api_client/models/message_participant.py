from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_participant_role import MessageParticipantRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_handle import ContactHandle


T = TypeVar("T", bound="MessageParticipant")


@_attrs_define
class MessageParticipant:
    """The name/handle pairs of the recipients, including to, cc, and bcc.

    Attributes:
        handle (ContactHandle): Handle of the contact. Can be any string used to uniquely identify the contact.
        role (MessageParticipantRole): Role of the participant
        name (Union[Unset, str]): Name of the participant. Used to create the contact if needed. Example: John Doe.
    """

    handle: "ContactHandle"
    role: MessageParticipantRole
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        handle = self.handle.to_dict()

        role = self.role.value

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "handle": handle,
                "role": role,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_handle import ContactHandle

        d = src_dict.copy()
        handle = ContactHandle.from_dict(d.pop("handle"))

        role = MessageParticipantRole(d.pop("role"))

        name = d.pop("name", UNSET)

        message_participant = cls(
            handle=handle,
            role=role,
            name=name,
        )

        message_participant.additional_properties = d
        return message_participant

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
