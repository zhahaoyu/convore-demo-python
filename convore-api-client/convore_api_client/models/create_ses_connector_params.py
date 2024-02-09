from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateSesConnectorParams")


@_attrs_define
class CreateSesConnectorParams:
    """SES configuration

    Attributes:
        access_key_id (str): The AWS access key ID of the user used to access SES and subscribe to the SNS topic
        secret_access_key (str): The AWS secret access key of the user used to access SES and subscribe to the SNS topic
        region (str): The region of the S3 bucket and SES connection
    """

    access_key_id: str
    secret_access_key: str
    region: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key_id = self.access_key_id

        secret_access_key = self.secret_access_key

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_key_id": access_key_id,
                "secret_access_key": secret_access_key,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_key_id = d.pop("access_key_id")

        secret_access_key = d.pop("secret_access_key")

        region = d.pop("region")

        create_ses_connector_params = cls(
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            region=region,
        )

        create_ses_connector_params.additional_properties = d
        return create_ses_connector_params

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
