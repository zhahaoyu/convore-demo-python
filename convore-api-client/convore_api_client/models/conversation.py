import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.conversation_priority import ConversationPriority
from ..models.conversation_status import ConversationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label import Label
    from ..models.message_participant import MessageParticipant


T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
    """
    Attributes:
        id (str): Unique identifier of the conversation. Example: conv_01h2xcejqtf2nbrexx3vqjhp41.
        channel_id (str): Identifier of the channel through which the conversation is taking place. Example:
            chnnl_01h2xcejqtf2nbrexx3vqjhp41.
        status (ConversationStatus): Status of the conversation
        priority (ConversationPriority): Priority of the conversation
        labels (List['Label']): List of labels for this conversation
        participants (List['MessageParticipant']):
        created_at (datetime.datetime): The ISO 8601 time at which the Conversation was created.
        subject (Union[Unset, str]): Subject of the conversation, if applicable. Null for non-email conversations.
            Example: Issue with Verification Process.
        snippet (Union[Unset, str]): A shortened plain-text preview of the message body.
        is_unread (Union[Unset, bool]): Whether the conversation has been read.
        last_message_date (Union[Unset, datetime.datetime]): ISO 8601 time of the most recent message.
        external_conversation_id (Union[Unset, str]): The identifier of the conversation in an external system.
        message_count (Union[Unset, int]): The number of messages in this conversation.
        draft_count (Union[Unset, int]): The number of drafts in this conversation.
        attachment_count (Union[Unset, int]): The number of attachments in this conversation.
    """

    id: str
    channel_id: str
    status: ConversationStatus
    priority: ConversationPriority
    labels: List["Label"]
    participants: List["MessageParticipant"]
    created_at: datetime.datetime
    subject: Union[Unset, str] = UNSET
    snippet: Union[Unset, str] = UNSET
    is_unread: Union[Unset, bool] = UNSET
    last_message_date: Union[Unset, datetime.datetime] = UNSET
    external_conversation_id: Union[Unset, str] = UNSET
    message_count: Union[Unset, int] = UNSET
    draft_count: Union[Unset, int] = UNSET
    attachment_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        channel_id = self.channel_id

        status = self.status.value

        priority = self.priority.value

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)

        participants = []
        for participants_item_data in self.participants:
            participants_item = participants_item_data.to_dict()
            participants.append(participants_item)

        created_at = self.created_at.isoformat()

        subject = self.subject

        snippet = self.snippet

        is_unread = self.is_unread

        last_message_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_message_date, Unset):
            last_message_date = self.last_message_date.isoformat()

        external_conversation_id = self.external_conversation_id

        message_count = self.message_count

        draft_count = self.draft_count

        attachment_count = self.attachment_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "channel_id": channel_id,
                "status": status,
                "priority": priority,
                "labels": labels,
                "participants": participants,
                "created_at": created_at,
            }
        )
        if subject is not UNSET:
            field_dict["subject"] = subject
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if is_unread is not UNSET:
            field_dict["is_unread"] = is_unread
        if last_message_date is not UNSET:
            field_dict["last_message_date"] = last_message_date
        if external_conversation_id is not UNSET:
            field_dict["external_conversation_id"] = external_conversation_id
        if message_count is not UNSET:
            field_dict["message_count"] = message_count
        if draft_count is not UNSET:
            field_dict["draft_count"] = draft_count
        if attachment_count is not UNSET:
            field_dict["attachment_count"] = attachment_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.label import Label
        from ..models.message_participant import MessageParticipant

        d = src_dict.copy()
        id = d.pop("id")

        channel_id = d.pop("channel_id")

        status = ConversationStatus(d.pop("status"))

        priority = ConversationPriority(d.pop("priority"))

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in _labels:
            labels_item = Label.from_dict(labels_item_data)

            labels.append(labels_item)

        participants = []
        _participants = d.pop("participants")
        for participants_item_data in _participants:
            participants_item = MessageParticipant.from_dict(participants_item_data)

            participants.append(participants_item)

        created_at = isoparse(d.pop("created_at"))

        subject = d.pop("subject", UNSET)

        snippet = d.pop("snippet", UNSET)

        is_unread = d.pop("is_unread", UNSET)

        _last_message_date = d.pop("last_message_date", UNSET)
        last_message_date: Union[Unset, datetime.datetime]
        if isinstance(_last_message_date, Unset):
            last_message_date = UNSET
        else:
            last_message_date = isoparse(_last_message_date)

        external_conversation_id = d.pop("external_conversation_id", UNSET)

        message_count = d.pop("message_count", UNSET)

        draft_count = d.pop("draft_count", UNSET)

        attachment_count = d.pop("attachment_count", UNSET)

        conversation = cls(
            id=id,
            channel_id=channel_id,
            status=status,
            priority=priority,
            labels=labels,
            participants=participants,
            created_at=created_at,
            subject=subject,
            snippet=snippet,
            is_unread=is_unread,
            last_message_date=last_message_date,
            external_conversation_id=external_conversation_id,
            message_count=message_count,
            draft_count=draft_count,
            attachment_count=attachment_count,
        )

        conversation.additional_properties = d
        return conversation

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
