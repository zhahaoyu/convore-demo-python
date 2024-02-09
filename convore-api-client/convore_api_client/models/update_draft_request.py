from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDraftRequest")


@_attrs_define
class UpdateDraftRequest:
    """
    Attributes:
        channel_id (Union[Unset, str]): Identifier of the channel through which the conversation is taking place.
            Example: chnnl_01h2xcejqtf2nbrexx3vqjhp41.
        from_ (Union[Unset, str]):
        to (Union[Unset, List[str]]):
        cc (Union[Unset, List[str]]):
        bcc (Union[Unset, List[str]]):
        subject (Union[Unset, str]): Subject of the email message, if applicable. Null for non-email conversations.
            Example: Re: Issue with Verification Process.
        body (Union[Unset, str]): The full HTML body of the message. Messages with only plain-text representations are
            up-converted to HTML. Example: ....
        quote_body (Union[Unset, str]): Body for the quote that the message is referencing. Only available on email
            channels. Example: On Dec 15, 2023, at 6:54 PM, John Doe <john@example.com> wrote: ....
    """

    channel_id: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    to: Union[Unset, List[str]] = UNSET
    cc: Union[Unset, List[str]] = UNSET
    bcc: Union[Unset, List[str]] = UNSET
    subject: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    quote_body: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_id = self.channel_id

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

        body = self.body

        quote_body = self.quote_body

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
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
        if body is not UNSET:
            field_dict["body"] = body
        if quote_body is not UNSET:
            field_dict["quote_body"] = quote_body

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = d.pop("channel_id", UNSET)

        from_ = d.pop("from", UNSET)

        to = cast(List[str], d.pop("to", UNSET))

        cc = cast(List[str], d.pop("cc", UNSET))

        bcc = cast(List[str], d.pop("bcc", UNSET))

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        quote_body = d.pop("quote_body", UNSET)

        update_draft_request = cls(
            channel_id=channel_id,
            from_=from_,
            to=to,
            cc=cc,
            bcc=bcc,
            subject=subject,
            body=body,
            quote_body=quote_body,
        )

        update_draft_request.additional_properties = d
        return update_draft_request

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
