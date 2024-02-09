import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.label_type import LabelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Label")


@_attrs_define
class Label:
    """
    Attributes:
        id (str): Unique identifier of the label. Example: lbl_01hggtgr3yfm3t450q1hq4vs9s.
        name (str): The human-readable name of the label, used for easy identification. This name can be something
            descriptive related to the label's purpose, like 'Technical Support' or 'Urgent'. Example: Technical support.
        created_at (datetime.datetime): The ISO 8601 time at which the Label was created.
        type (LabelType): The type of the label, which determines its scope and usage. 'SHARED' labels are accessible
            across multiple channels, while 'CHANNEL_PRIVATE' labels are restricted to a specific channel. Note: When a
            'SHARED' label is created and later applied to a conversation, the API automatically applies the corresponding
            'CHANNEL_PRIVATE' label to the conversation in the specific channel, and vice versa. Example: SHARED.
        description (Union[Unset, str]): An optional detailed description of the label, providing additional context
            about its purpose. Example: Help with website or app functionality, technical glitches, and navigation..
        channel_id (Union[Unset, str]): The identifier of the channel this label is associated with, required for
            CHANNEL_PRIVATE labels. This links the label to a specific communication channel. Example:
            chnnl_01h2xcejqtf2nbrexx3vqjhp41.
        external_label_id (Union[Unset, str]): Identifier of the label in an external system, required for
            CHANNEL_PRIVATE labels that map to external systems. Example: ext_lbl_23kj2b3k4j2.
        shared_label_id (Union[Unset, str]): An identifier used to associate this CHANNEL_PRIVATE label with a
            corresponding SHARED label within the organization, facilitating unified label management across different
            channels.
    """

    id: str
    name: str
    created_at: datetime.datetime
    type: LabelType
    description: Union[Unset, str] = UNSET
    channel_id: Union[Unset, str] = UNSET
    external_label_id: Union[Unset, str] = UNSET
    shared_label_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        created_at = self.created_at.isoformat()

        type = self.type.value

        description = self.description

        channel_id = self.channel_id

        external_label_id = self.external_label_id

        shared_label_id = self.shared_label_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "type": type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if external_label_id is not UNSET:
            field_dict["external_label_id"] = external_label_id
        if shared_label_id is not UNSET:
            field_dict["shared_label_id"] = shared_label_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        type = LabelType(d.pop("type"))

        description = d.pop("description", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        external_label_id = d.pop("external_label_id", UNSET)

        shared_label_id = d.pop("shared_label_id", UNSET)

        label = cls(
            id=id,
            name=name,
            created_at=created_at,
            type=type,
            description=description,
            channel_id=channel_id,
            external_label_id=external_label_id,
            shared_label_id=shared_label_id,
        )

        label.additional_properties = d
        return label

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
