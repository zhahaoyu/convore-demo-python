from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSesConnectorParams")


@_attrs_define
class UpdateSesConnectorParams:
    """SES configuration. Only the non-null fields are set

    Attributes:
        access_key_id (Union[Unset, str]): The AWS access key ID of the user used to access SES and subscribe to the SNS
            topic
        secret_access_key (Union[Unset, str]): The AWS secret access key of the user used to access SES and subscribe to
            the SNS topic
        region (Union[Unset, str]): The region of the S3 bucket and SES connection
    """

    access_key_id: Union[Unset, str] = UNSET
    secret_access_key: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key_id = self.access_key_id

        secret_access_key = self.secret_access_key

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key_id is not UNSET:
            field_dict["access_key_id"] = access_key_id
        if secret_access_key is not UNSET:
            field_dict["secret_access_key"] = secret_access_key
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_key_id = d.pop("access_key_id", UNSET)

        secret_access_key = d.pop("secret_access_key", UNSET)

        region = d.pop("region", UNSET)

        update_ses_connector_params = cls(
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            region=region,
        )

        update_ses_connector_params.additional_properties = d
        return update_ses_connector_params

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
