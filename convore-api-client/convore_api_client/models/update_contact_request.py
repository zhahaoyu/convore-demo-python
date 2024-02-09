from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_handle import ContactHandle


T = TypeVar("T", bound="UpdateContactRequest")


@_attrs_define
class UpdateContactRequest:
    """
    Attributes:
        name (Union[Unset, str]): Contact name. Example: John Doe.
        description (Union[Unset, str]): Contact description. Example: Head of Sales, Acme Corp..
        handles (Union[Unset, List['ContactHandle']]): List of the handles for this contact.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    handles: Union[Unset, List["ContactHandle"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        handles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.handles, Unset):
            handles = []
            for handles_item_data in self.handles:
                handles_item = handles_item_data.to_dict()
                handles.append(handles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if handles is not UNSET:
            field_dict["handles"] = handles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_handle import ContactHandle

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        handles = []
        _handles = d.pop("handles", UNSET)
        for handles_item_data in _handles or []:
            handles_item = ContactHandle.from_dict(handles_item_data)

            handles.append(handles_item)

        update_contact_request = cls(
            name=name,
            description=description,
            handles=handles,
        )

        update_contact_request.additional_properties = d
        return update_contact_request

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
