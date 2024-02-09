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
from convore_api_client.models.channel_address import ChannelAddress
from convore_api_client.models.channel_status import ChannelStatus
from convore_api_client.models.convore_mail_channel import ConvoreMailChannel
from convore_api_client.models.provider_type import ProviderType
from convore_api_client.models.ses_channel import SesChannel
from typing import Optional, Set
from typing_extensions import Self

class Channel(BaseModel):
    """
    Channel
    """ # noqa: E501
    id: StrictStr = Field(description="Unique identifier for the channel")
    connector_id: StrictStr = Field(description="Unique identifier for the channel's connector")
    provider: ProviderType
    name: StrictStr = Field(description="Name of the channel")
    addresses: List[ChannelAddress] = Field(description="A collection of communication addresses associated with the channel. These addresses are used for sending and receiving messages, ensuring proper routing and delivery of content. Each address specifies a unique handle, such as an email or a phone number, along with associated details like the participant's name and role.")
    status: ChannelStatus
    created_at: datetime = Field(description="The ISO 8601 time at which the Channel was created.")
    convore_mail: Optional[ConvoreMailChannel] = None
    ses: Optional[SesChannel] = None
    __properties: ClassVar[List[str]] = ["id", "connector_id", "provider", "name", "addresses", "status", "created_at", "convore_mail", "ses"]

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
        """Create an instance of Channel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in addresses (list)
        _items = []
        if self.addresses:
            for _item in self.addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of convore_mail
        if self.convore_mail:
            _dict['convore_mail'] = self.convore_mail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ses
        if self.ses:
            _dict['ses'] = self.ses.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Channel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "connector_id": obj.get("connector_id"),
            "provider": obj.get("provider"),
            "name": obj.get("name"),
            "addresses": [ChannelAddress.from_dict(_item) for _item in obj["addresses"]] if obj.get("addresses") is not None else None,
            "status": obj.get("status"),
            "created_at": obj.get("created_at"),
            "convore_mail": ConvoreMailChannel.from_dict(obj["convore_mail"]) if obj.get("convore_mail") is not None else None,
            "ses": SesChannel.from_dict(obj["ses"]) if obj.get("ses") is not None else None
        })
        return _obj


