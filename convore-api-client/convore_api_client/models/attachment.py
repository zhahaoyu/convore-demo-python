from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Attachment")


@_attrs_define
class Attachment:
    """An array of Attachment objects.

    Attributes:
        id (str): Unique identifier of the attachment. Example: attch_01hcf9x766fqk8g7hz74363j9q.
        conversation_id (str): Conversation ID of the conversation the attachment belongs to.. Example:
            conv_01h2xcejqtf2nbrexx3vqjhp41.
        content_type (str): MIME type of the attachment (e.g., image/png, application/pdf). Example: image/png.
        filename (str): Original filename of the attachment. Example: image.png.
        is_inline (bool): Only applies to Email messages. Indicates if the attachment is displayed inline (using CID)
            within the message content or as a regular attachment.
        size (int): Size of the attachment in bytes. Example: 14039.
        draft_id (Union[Unset, str]): Draft ID of the draft the attachment belongs to. Either this or message_id must be
            provided, but not both. Example: drft_01h2xcejqtf2nbrexx3vqjhp41.
        message_id (Union[Unset, str]): Message ID of the message the attachment belongs to. Either this or draft_id
            must be provided, but not both.
    """

    id: str
    conversation_id: str
    content_type: str
    filename: str
    is_inline: bool
    size: int
    draft_id: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        conversation_id = self.conversation_id

        content_type = self.content_type

        filename = self.filename

        is_inline = self.is_inline

        size = self.size

        draft_id = self.draft_id

        message_id = self.message_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "conversation_id": conversation_id,
                "content_type": content_type,
                "filename": filename,
                "is_inline": is_inline,
                "size": size,
            }
        )
        if draft_id is not UNSET:
            field_dict["draft_id"] = draft_id
        if message_id is not UNSET:
            field_dict["message_id"] = message_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        conversation_id = d.pop("conversation_id")

        content_type = d.pop("content_type")

        filename = d.pop("filename")

        is_inline = d.pop("is_inline")

        size = d.pop("size")

        draft_id = d.pop("draft_id", UNSET)

        message_id = d.pop("message_id", UNSET)

        attachment = cls(
            id=id,
            conversation_id=conversation_id,
            content_type=content_type,
            filename=filename,
            is_inline=is_inline,
            size=size,
            draft_id=draft_id,
            message_id=message_id,
        )

        attachment.additional_properties = d
        return attachment

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
