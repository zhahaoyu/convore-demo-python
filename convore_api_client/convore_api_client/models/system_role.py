# coding: utf-8

"""
    Convore API

    Convore API v1.0.0

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SystemRole(str, Enum):
    """
    SystemRole
    """

    """
    allowed enum values
    """
    USER = 'user'
    SUPER_ADMIN = 'super_admin'
    ORGANIZATION = 'organization'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SystemRole from a JSON string"""
        return cls(json.loads(json_str))


