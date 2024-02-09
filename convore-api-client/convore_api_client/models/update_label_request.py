from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateLabelRequest")


@_attrs_define
class UpdateLabelRequest:
    """
    Attributes:
        name (Union[Unset, str]): Name of the label. Example: Technical support.
        description (Union[Unset, str]): Help with website or app functionality, technical glitches, and navigation.
            Example: Urgent and important.
        shared_label_id (Union[Unset, str]): An identifier used to associate a CHANNEL_PRIVATE label with a
            corresponding SHARED label within the organization, facilitating unified label management across different
            channels.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    shared_label_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        shared_label_id = self.shared_label_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if shared_label_id is not UNSET:
            field_dict["shared_label_id"] = shared_label_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        shared_label_id = d.pop("shared_label_id", UNSET)

        update_label_request = cls(
            name=name,
            description=description,
            shared_label_id=shared_label_id,
        )

        update_label_request.additional_properties = d
        return update_label_request

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
