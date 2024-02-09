from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_handle import ContactHandle


T = TypeVar("T", bound="CreateContactRequest")


@_attrs_define
class CreateContactRequest:
    """
    Attributes:
        name (str): Contact name. Example: John Doe.
        handles (List['ContactHandle']): List of the handles for this contact.
        description (Union[Unset, str]): Contact description. Example: Head of Sales, Acme Corp..
    """

    name: str
    handles: List["ContactHandle"]
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        handles = []
        for handles_item_data in self.handles:
            handles_item = handles_item_data.to_dict()
            handles.append(handles_item)

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "handles": handles,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_handle import ContactHandle

        d = src_dict.copy()
        name = d.pop("name")

        handles = []
        _handles = d.pop("handles")
        for handles_item_data in _handles:
            handles_item = ContactHandle.from_dict(handles_item_data)

            handles.append(handles_item)

        description = d.pop("description", UNSET)

        create_contact_request = cls(
            name=name,
            handles=handles,
            description=description,
        )

        create_contact_request.additional_properties = d
        return create_contact_request

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
