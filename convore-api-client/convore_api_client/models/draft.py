import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.message_reply_type import MessageReplyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment
    from ..models.message_participant import MessageParticipant


T = TypeVar("T", bound="Draft")


@_attrs_define
class Draft:
    """
    Attributes:
        id (str): Unique identifier of the draft. Example: drft_01h2xcejqtf2nbrexx3vqjhp41.
        channel_id (str): Identifier of the channel through which the conversation is taking place. Example:
            chnnl_01h2xcejqtf2nbrexx3vqjhp41.
        conversation_id (str): Identifier of the conversation the draft belongs to. Example:
            chnnl_01h2xcejqtf2nbrexx3vqjhp41.
        sender (MessageParticipant): The name/handle pairs of the recipients, including to, cc, and bcc.
        recipients (List['MessageParticipant']): The name/handle pairs of the recipients, including to, cc, and bcc.
        attachments (List['Attachment']): An array of Attachment objects.
        created_at (datetime.datetime): The ISO 8601 time at which the Draft was created.
        message_id (Union[Unset, str]): The ID of the message created by the draft. Example:
            msg_01h2xcejqtf2nbrexx3vqjhp41.
        reply_to_message_id (Union[Unset, str]): The ID of the message that you're replying to. Example:
            msg_01h2xcejqtf2nbrexx3vqjhp41.
        reply_type (Union[Unset, MessageReplyType]): The type of reply that you're sending. If not provided, the channel
            will determine the reply type.
        subject (Union[Unset, str]): Subject of the email message, if applicable. Null for non-email conversations.
            Example: Issue with Verification Process.
        body (Union[Unset, str]): The full HTML body of the message. Messages with only plain-text representations are
            up-converted to HTML. Example: ....
        quote_body (Union[Unset, str]): Body for the quote that the message is referencing. Only available on email
            channels. Example: On Dec 15, 2023, at 6:54 PM, John Doe <john@example.com> wrote: ....
        external_draft_id (Union[Unset, str]): The identifier of the draft in an external system.
    """

    id: str
    channel_id: str
    conversation_id: str
    sender: "MessageParticipant"
    recipients: List["MessageParticipant"]
    attachments: List["Attachment"]
    created_at: datetime.datetime
    message_id: Union[Unset, str] = UNSET
    reply_to_message_id: Union[Unset, str] = UNSET
    reply_type: Union[Unset, MessageReplyType] = UNSET
    subject: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    quote_body: Union[Unset, str] = UNSET
    external_draft_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        channel_id = self.channel_id

        conversation_id = self.conversation_id

        sender = self.sender.to_dict()

        recipients = []
        for recipients_item_data in self.recipients:
            recipients_item = recipients_item_data.to_dict()
            recipients.append(recipients_item)

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        created_at = self.created_at.isoformat()

        message_id = self.message_id

        reply_to_message_id = self.reply_to_message_id

        reply_type: Union[Unset, str] = UNSET
        if not isinstance(self.reply_type, Unset):
            reply_type = self.reply_type.value

        subject = self.subject

        body = self.body

        quote_body = self.quote_body

        external_draft_id = self.external_draft_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "channel_id": channel_id,
                "conversation_id": conversation_id,
                "sender": sender,
                "recipients": recipients,
                "attachments": attachments,
                "created_at": created_at,
            }
        )
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if reply_to_message_id is not UNSET:
            field_dict["reply_to_message_id"] = reply_to_message_id
        if reply_type is not UNSET:
            field_dict["reply_type"] = reply_type
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if quote_body is not UNSET:
            field_dict["quote_body"] = quote_body
        if external_draft_id is not UNSET:
            field_dict["external_draft_id"] = external_draft_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attachment import Attachment
        from ..models.message_participant import MessageParticipant

        d = src_dict.copy()
        id = d.pop("id")

        channel_id = d.pop("channel_id")

        conversation_id = d.pop("conversation_id")

        sender = MessageParticipant.from_dict(d.pop("sender"))

        recipients = []
        _recipients = d.pop("recipients")
        for recipients_item_data in _recipients:
            recipients_item = MessageParticipant.from_dict(recipients_item_data)

            recipients.append(recipients_item)

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = Attachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        created_at = isoparse(d.pop("created_at"))

        message_id = d.pop("message_id", UNSET)

        reply_to_message_id = d.pop("reply_to_message_id", UNSET)

        _reply_type = d.pop("reply_type", UNSET)
        reply_type: Union[Unset, MessageReplyType]
        if isinstance(_reply_type, Unset):
            reply_type = UNSET
        else:
            reply_type = MessageReplyType(_reply_type)

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        quote_body = d.pop("quote_body", UNSET)

        external_draft_id = d.pop("external_draft_id", UNSET)

        draft = cls(
            id=id,
            channel_id=channel_id,
            conversation_id=conversation_id,
            sender=sender,
            recipients=recipients,
            attachments=attachments,
            created_at=created_at,
            message_id=message_id,
            reply_to_message_id=reply_to_message_id,
            reply_type=reply_type,
            subject=subject,
            body=body,
            quote_body=quote_body,
            external_draft_id=external_draft_id,
        )

        draft.additional_properties = d
        return draft

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
