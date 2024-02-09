import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.message_direction import MessageDirection
from ..models.message_reply_type import MessageReplyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_participant import MessageParticipant


T = TypeVar("T", bound="ImportMessageRequest")


@_attrs_define
class ImportMessageRequest:
    """
    Attributes:
        date (datetime.datetime): ISO 8601 time of when the message was sent.
        sender (MessageParticipant): The name/handle pairs of the recipients, including to, cc, and bcc.
        recipients (List['MessageParticipant']):
        conversation_id (Union[Unset, str]): Identifier of the conversation the message belongs to. Either
            conversationId or channelId must be provided. Example: conv_01h2xcejqtf2nbrexx3vqjhp41.
        channel_id (Union[Unset, str]): Identifier of the channel through which the conversation is taking place. Either
            conversationId or channelId must be provided. Example: chnnl_01h2xcejqtf2nbrexx3vqjhp41.
        subject (Union[Unset, str]): Subject of the email message, if applicable. Null for non-email conversations.
            Example: Issue with Verification Process.
        direction (Union[Unset, MessageDirection]): Whether the message is inbound or outbound.
        body (Union[Unset, str]):
        snippet (Union[Unset, str]):
        reply_to_message_id (Union[Unset, str]): The ID of the message that you're replying to. Example:
            msg_01h2xcejqtf2nbrexx3vqjhp41.
        reply_type (Union[Unset, MessageReplyType]): The type of reply that you're sending. If not provided, the channel
            will determine the reply type.
    """

    date: datetime.datetime
    sender: "MessageParticipant"
    recipients: List["MessageParticipant"]
    conversation_id: Union[Unset, str] = UNSET
    channel_id: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    direction: Union[Unset, MessageDirection] = UNSET
    body: Union[Unset, str] = UNSET
    snippet: Union[Unset, str] = UNSET
    reply_to_message_id: Union[Unset, str] = UNSET
    reply_type: Union[Unset, MessageReplyType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date.isoformat()

        sender = self.sender.to_dict()

        recipients = []
        for recipients_item_data in self.recipients:
            recipients_item = recipients_item_data.to_dict()
            recipients.append(recipients_item)

        conversation_id = self.conversation_id

        channel_id = self.channel_id

        subject = self.subject

        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        body = self.body

        snippet = self.snippet

        reply_to_message_id = self.reply_to_message_id

        reply_type: Union[Unset, str] = UNSET
        if not isinstance(self.reply_type, Unset):
            reply_type = self.reply_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "sender": sender,
                "recipients": recipients,
            }
        )
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if subject is not UNSET:
            field_dict["subject"] = subject
        if direction is not UNSET:
            field_dict["direction"] = direction
        if body is not UNSET:
            field_dict["body"] = body
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if reply_to_message_id is not UNSET:
            field_dict["reply_to_message_id"] = reply_to_message_id
        if reply_type is not UNSET:
            field_dict["reply_type"] = reply_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message_participant import MessageParticipant

        d = src_dict.copy()
        date = isoparse(d.pop("date"))

        sender = MessageParticipant.from_dict(d.pop("sender"))

        recipients = []
        _recipients = d.pop("recipients")
        for recipients_item_data in _recipients:
            recipients_item = MessageParticipant.from_dict(recipients_item_data)

            recipients.append(recipients_item)

        conversation_id = d.pop("conversation_id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        subject = d.pop("subject", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, MessageDirection]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = MessageDirection(_direction)

        body = d.pop("body", UNSET)

        snippet = d.pop("snippet", UNSET)

        reply_to_message_id = d.pop("reply_to_message_id", UNSET)

        _reply_type = d.pop("reply_type", UNSET)
        reply_type: Union[Unset, MessageReplyType]
        if isinstance(_reply_type, Unset):
            reply_type = UNSET
        else:
            reply_type = MessageReplyType(_reply_type)

        import_message_request = cls(
            date=date,
            sender=sender,
            recipients=recipients,
            conversation_id=conversation_id,
            channel_id=channel_id,
            subject=subject,
            direction=direction,
            body=body,
            snippet=snippet,
            reply_to_message_id=reply_to_message_id,
            reply_type=reply_type,
        )

        import_message_request.additional_properties = d
        return import_message_request

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
