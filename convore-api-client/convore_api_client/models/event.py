import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.event_type import EventType
from ..models.object_type import ObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        id (str): Unique identifier of the event. Example: event_01hggtpfewf0y91nde7cz02p0k.
        type (EventType):
        object_id (str): The ID of the object associated with the event. Example: conv_01h2xcejqtf2nbrexx3vqjhp41.
        object_type (ObjectType):
        created_at (datetime.datetime): The ISO 8601 time at which the Event was created.
        conversation_id (Union[Unset, str]): The ID of the conversation associated with the event.
        message_id (Union[Unset, str]): The ID of the message associated with the event.
        label_id (Union[Unset, str]): The ID of the label associated with the event.
    """

    id: str
    type: EventType
    object_id: str
    object_type: ObjectType
    created_at: datetime.datetime
    conversation_id: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    label_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        object_id = self.object_id

        object_type = self.object_type.value

        created_at = self.created_at.isoformat()

        conversation_id = self.conversation_id

        message_id = self.message_id

        label_id = self.label_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "object_id": object_id,
                "object_type": object_type,
                "created_at": created_at,
            }
        )
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if label_id is not UNSET:
            field_dict["label_id"] = label_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = EventType(d.pop("type"))

        object_id = d.pop("object_id")

        object_type = ObjectType(d.pop("object_type"))

        created_at = isoparse(d.pop("created_at"))

        conversation_id = d.pop("conversation_id", UNSET)

        message_id = d.pop("message_id", UNSET)

        label_id = d.pop("label_id", UNSET)

        event = cls(
            id=id,
            type=type,
            object_id=object_id,
            object_type=object_type,
            created_at=created_at,
            conversation_id=conversation_id,
            message_id=message_id,
            label_id=label_id,
        )

        event.additional_properties = d
        return event

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
