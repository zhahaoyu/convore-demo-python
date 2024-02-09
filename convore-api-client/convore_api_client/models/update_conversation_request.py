import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.conversation_priority import ConversationPriority
from ..models.conversation_status import ConversationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_participant import MessageParticipant


T = TypeVar("T", bound="UpdateConversationRequest")


@_attrs_define
class UpdateConversationRequest:
    """
    Attributes:
        status (Union[Unset, ConversationStatus]): Status of the conversation
        priority (Union[Unset, ConversationPriority]): Priority of the conversation
        label_ids (Union[Unset, List[str]]): List of labels for this conversation
        participants (Union[Unset, List['MessageParticipant']]):
        subject (Union[Unset, str]): Subject of the conversation, if applicable. Null for non-email conversations.
            Example: Issue with Verification Process.
        snippet (Union[Unset, str]): A shortened plain-text preview of the message body.
        is_unread (Union[Unset, bool]): Whether the conversation has been read.
        last_message_date (Union[Unset, datetime.datetime]): ISO 8601 time of the most recent message.
    """

    status: Union[Unset, ConversationStatus] = UNSET
    priority: Union[Unset, ConversationPriority] = UNSET
    label_ids: Union[Unset, List[str]] = UNSET
    participants: Union[Unset, List["MessageParticipant"]] = UNSET
    subject: Union[Unset, str] = UNSET
    snippet: Union[Unset, str] = UNSET
    is_unread: Union[Unset, bool] = UNSET
    last_message_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        label_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids

        participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

        subject = self.subject

        snippet = self.snippet

        is_unread = self.is_unread

        last_message_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_message_date, Unset):
            last_message_date = self.last_message_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if priority is not UNSET:
            field_dict["priority"] = priority
        if label_ids is not UNSET:
            field_dict["label_ids"] = label_ids
        if participants is not UNSET:
            field_dict["participants"] = participants
        if subject is not UNSET:
            field_dict["subject"] = subject
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if is_unread is not UNSET:
            field_dict["is_unread"] = is_unread
        if last_message_date is not UNSET:
            field_dict["last_message_date"] = last_message_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message_participant import MessageParticipant

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, ConversationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ConversationStatus(_status)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, ConversationPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = ConversationPriority(_priority)

        label_ids = cast(List[str], d.pop("label_ids", UNSET))

        participants = []
        _participants = d.pop("participants", UNSET)
        for participants_item_data in _participants or []:
            participants_item = MessageParticipant.from_dict(participants_item_data)

            participants.append(participants_item)

        subject = d.pop("subject", UNSET)

        snippet = d.pop("snippet", UNSET)

        is_unread = d.pop("is_unread", UNSET)

        _last_message_date = d.pop("last_message_date", UNSET)
        last_message_date: Union[Unset, datetime.datetime]
        if isinstance(_last_message_date, Unset):
            last_message_date = UNSET
        else:
            last_message_date = isoparse(_last_message_date)

        update_conversation_request = cls(
            status=status,
            priority=priority,
            label_ids=label_ids,
            participants=participants,
            subject=subject,
            snippet=snippet,
            is_unread=is_unread,
            last_message_date=last_message_date,
        )

        update_conversation_request.additional_properties = d
        return update_conversation_request

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
