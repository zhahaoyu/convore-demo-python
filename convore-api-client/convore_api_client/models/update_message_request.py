import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.message_direction import MessageDirection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_participant import MessageParticipant


T = TypeVar("T", bound="UpdateMessageRequest")


@_attrs_define
class UpdateMessageRequest:
    """
    Attributes:
        subject (Union[Unset, str]): Subject of the email message, if applicable. Null for non-email conversations.
            Example: Issue with Verification Process.
        direction (Union[Unset, MessageDirection]): Whether the message is inbound or outbound.
        date (Union[Unset, datetime.datetime]):
        sender (Union[Unset, MessageParticipant]): The name/handle pairs of the recipients, including to, cc, and bcc.
        recipients (Union[Unset, List['MessageParticipant']]):
        body (Union[Unset, str]):
        snippet (Union[Unset, str]):
    """

    subject: Union[Unset, str] = UNSET
    direction: Union[Unset, MessageDirection] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    sender: Union[Unset, "MessageParticipant"] = UNSET
    recipients: Union[Unset, List["MessageParticipant"]] = UNSET
    body: Union[Unset, str] = UNSET
    snippet: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject

        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        sender: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        recipients: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = []
            for recipients_item_data in self.recipients:
                recipients_item = recipients_item_data.to_dict()
                recipients.append(recipients_item)

        body = self.body

        snippet = self.snippet

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject is not UNSET:
            field_dict["subject"] = subject
        if direction is not UNSET:
            field_dict["direction"] = direction
        if date is not UNSET:
            field_dict["date"] = date
        if sender is not UNSET:
            field_dict["sender"] = sender
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if body is not UNSET:
            field_dict["body"] = body
        if snippet is not UNSET:
            field_dict["snippet"] = snippet

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message_participant import MessageParticipant

        d = src_dict.copy()
        subject = d.pop("subject", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, MessageDirection]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = MessageDirection(_direction)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _sender = d.pop("sender", UNSET)
        sender: Union[Unset, MessageParticipant]
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = MessageParticipant.from_dict(_sender)

        recipients = []
        _recipients = d.pop("recipients", UNSET)
        for recipients_item_data in _recipients or []:
            recipients_item = MessageParticipant.from_dict(recipients_item_data)

            recipients.append(recipients_item)

        body = d.pop("body", UNSET)

        snippet = d.pop("snippet", UNSET)

        update_message_request = cls(
            subject=subject,
            direction=direction,
            date=date,
            sender=sender,
            recipients=recipients,
            body=body,
            snippet=snippet,
        )

        update_message_request.additional_properties = d
        return update_message_request

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
