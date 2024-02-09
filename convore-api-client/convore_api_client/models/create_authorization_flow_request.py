from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateAuthorizationFlowRequest")


@_attrs_define
class CreateAuthorizationFlowRequest:
    """
    Attributes:
        connector_id (str):
        success_redirect_uri (str):
        error_redirect_uri (str):
    """

    connector_id: str
    success_redirect_uri: str
    error_redirect_uri: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connector_id = self.connector_id

        success_redirect_uri = self.success_redirect_uri

        error_redirect_uri = self.error_redirect_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connector_id": connector_id,
                "success_redirect_uri": success_redirect_uri,
                "error_redirect_uri": error_redirect_uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connector_id = d.pop("connector_id")

        success_redirect_uri = d.pop("success_redirect_uri")

        error_redirect_uri = d.pop("error_redirect_uri")

        create_authorization_flow_request = cls(
            connector_id=connector_id,
            success_redirect_uri=success_redirect_uri,
            error_redirect_uri=error_redirect_uri,
        )

        create_authorization_flow_request.additional_properties = d
        return create_authorization_flow_request

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
