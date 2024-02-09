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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from convore_api_client.models.contact_handle import ContactHandle
from typing import Optional, Set
from typing_extensions import Self

class ChannelAddress(BaseModel):
    """
    A collection of communication addresses associated with the channel. These addresses are used for sending and receiving messages, ensuring proper routing and delivery of content. Each address specifies a unique handle, such as an email or a phone number, along with associated details like the participant's name and role.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Name of the sender.")
    handle: ContactHandle
    is_primary: Optional[StrictBool] = Field(default=None, description="Whether the address is the primary address for the channel.")
    __properties: ClassVar[List[str]] = ["name", "handle", "is_primary"]

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
        """Create an instance of ChannelAddress from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of handle
        if self.handle:
            _dict['handle'] = self.handle.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChannelAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "handle": ContactHandle.from_dict(obj["handle"]) if obj.get("handle") is not None else None,
            "is_primary": obj.get("is_primary")
        })
        return _obj


