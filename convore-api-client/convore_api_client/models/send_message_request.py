from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_reply_type import MessageReplyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendMessageRequest")


@_attrs_define
class SendMessageRequest:
    """
    Attributes:
        body (str): The full HTML body of the message. Messages with only plain-text representations are up-converted to
            HTML. Example: ....
        channel_id (Union[Unset, str]): Identifier of the channel through which the conversation is taking place. Either
            channelId or replyToMessageId must be provided. Example: chnnl_01h2xcejqtf2nbrexx3vqjhp41.
        conversation_id (Union[Unset, str]): Identifier of the conversation the message belongs to. Example:
            conv_01h2xcejqtf2nbrexx3vqjhp41.
        reply_to_message_id (Union[Unset, str]): The ID of the message that you're replying to. Either channelId or
            replyToMessageId must be provided Example: msg_01h2xcejqtf2nbrexx3vqjhp41.
        reply_type (Union[Unset, MessageReplyType]): The type of reply that you're sending. If not provided, the channel
            will determine the reply type.
        from_ (Union[Unset, str]):
        to (Union[Unset, List[str]]):
        cc (Union[Unset, List[str]]):
        bcc (Union[Unset, List[str]]):
        subject (Union[Unset, str]): Subject of the email message, if applicable. Null for non-email conversations.
            Example: Re: Issue with Verification Process.
        quote_body (Union[Unset, str]): Body for the quote that the message is referencing. Only available on email
            channels. Example: On Dec 15, 2023, at 6:54 PM, John Doe <john@example.com> wrote: ....
    """

    body: str
    channel_id: Union[Unset, str] = UNSET
    conversation_id: Union[Unset, str] = UNSET
    reply_to_message_id: Union[Unset, str] = UNSET
    reply_type: Union[Unset, MessageReplyType] = UNSET
    from_: Union[Unset, str] = UNSET
    to: Union[Unset, List[str]] = UNSET
    cc: Union[Unset, List[str]] = UNSET
    bcc: Union[Unset, List[str]] = UNSET
    subject: Union[Unset, str] = UNSET
    quote_body: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body

        channel_id = self.channel_id

        conversation_id = self.conversation_id

        reply_to_message_id = self.reply_to_message_id

        reply_type: Union[Unset, str] = UNSET
        if not isinstance(self.reply_type, Unset):
            reply_type = self.reply_type.value

        from_ = self.from_

        to: Union[Unset, List[str]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to

        cc: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cc, Unset):
            cc = self.cc

        bcc: Union[Unset, List[str]] = UNSET
        if not isinstance(self.bcc, Unset):
            bcc = self.bcc

        subject = self.subject

        quote_body = self.quote_body

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
            }
        )
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if reply_to_message_id is not UNSET:
            field_dict["reply_to_message_id"] = reply_to_message_id
        if reply_type is not UNSET:
            field_dict["reply_type"] = reply_type
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if cc is not UNSET:
            field_dict["cc"] = cc
        if bcc is not UNSET:
            field_dict["bcc"] = bcc
        if subject is not UNSET:
            field_dict["subject"] = subject
        if quote_body is not UNSET:
            field_dict["quote_body"] = quote_body

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        body = d.pop("body")

        channel_id = d.pop("channel_id", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        reply_to_message_id = d.pop("reply_to_message_id", UNSET)

        _reply_type = d.pop("reply_type", UNSET)
        reply_type: Union[Unset, MessageReplyType]
        if isinstance(_reply_type, Unset):
            reply_type = UNSET
        else:
            reply_type = MessageReplyType(_reply_type)

        from_ = d.pop("from", UNSET)

        to = cast(List[str], d.pop("to", UNSET))

        cc = cast(List[str], d.pop("cc", UNSET))

        bcc = cast(List[str], d.pop("bcc", UNSET))

        subject = d.pop("subject", UNSET)

        quote_body = d.pop("quote_body", UNSET)

        send_message_request = cls(
            body=body,
            channel_id=channel_id,
            conversation_id=conversation_id,
            reply_to_message_id=reply_to_message_id,
            reply_type=reply_type,
            from_=from_,
            to=to,
            cc=cc,
            bcc=bcc,
            subject=subject,
            quote_body=quote_body,
        )

        send_message_request.additional_properties = d
        return send_message_request

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
