# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from convore_api_client.models.attachment import Attachment
from convore_api_client.models.message_participant import MessageParticipant
from convore_api_client.models.message_reply_type import MessageReplyType
from typing import Optional, Set
from typing_extensions import Self

class Draft(BaseModel):
    """
    Draft
    """ # noqa: E501
    id: StrictStr = Field(description="Unique identifier of the draft.")
    channel_id: StrictStr = Field(description="Identifier of the channel through which the conversation is taking place.")
    conversation_id: StrictStr = Field(description="Identifier of the conversation the draft belongs to.")
    message_id: Optional[StrictStr] = Field(default=None, description="The ID of the message created by the draft.")
    reply_to_message_id: Optional[StrictStr] = Field(default=None, description="The ID of the message that you're replying to.")
    reply_type: Optional[MessageReplyType] = None
    sender: MessageParticipant
    recipients: List[MessageParticipant] = Field(description="The name/handle pairs of the recipients, including to, cc, and bcc.")
    subject: Optional[StrictStr] = Field(default=None, description="Subject of the email message, if applicable. Null for non-email conversations.")
    raw_body: Optional[StrictStr] = Field(default=None, description="The full HTML body of the message. Messages with only plain-text representations are up-converted to HTML.")
    body: Optional[StrictStr] = Field(default=None, description="The full HTML body of the message without quotations.")
    quote_body: Optional[StrictStr] = Field(default=None, description="Body for the quote that the message is referencing. Only available on email channels.")
    attachments: List[Attachment] = Field(description="An array of Attachment objects.")
    external_draft_id: Optional[StrictStr] = Field(default=None, description="The identifier of the draft in an external system.")
    created_at: datetime = Field(description="The ISO 8601 time at which the Draft was created.")
    __properties: ClassVar[List[str]] = ["id", "channel_id", "conversation_id", "message_id", "reply_to_message_id", "reply_type", "sender", "recipients", "subject", "raw_body", "body", "quote_body", "attachments", "external_draft_id", "created_at"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Draft from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of sender
        if self.sender:
            _dict['sender'] = self.sender.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in recipients (list)
        _items = []
        if self.recipients:
            for _item in self.recipients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recipients'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item in self.attachments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attachments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Draft from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "channel_id": obj.get("channel_id"),
            "conversation_id": obj.get("conversation_id"),
            "message_id": obj.get("message_id"),
            "reply_to_message_id": obj.get("reply_to_message_id"),
            "reply_type": obj.get("reply_type"),
            "sender": MessageParticipant.from_dict(obj["sender"]) if obj.get("sender") is not None else None,
            "recipients": [MessageParticipant.from_dict(_item) for _item in obj["recipients"]] if obj.get("recipients") is not None else None,
            "subject": obj.get("subject"),
            "raw_body": obj.get("raw_body"),
            "body": obj.get("body"),
            "quote_body": obj.get("quote_body"),
            "attachments": [Attachment.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "external_draft_id": obj.get("external_draft_id"),
            "created_at": obj.get("created_at")
        })
        return _obj


