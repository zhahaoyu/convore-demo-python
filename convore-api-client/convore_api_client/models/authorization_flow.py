from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.authorization_flow_status import AuthorizationFlowStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorizationFlow")


@_attrs_define
class AuthorizationFlow:
    """
    Attributes:
        id (str):
        connector_id (str):
        success_redirect_uri (str):
        error_redirect_uri (str):
        status (AuthorizationFlowStatus):
        grant_url (str):
        connected_channel_id (Union[Unset, str]):
    """

    id: str
    connector_id: str
    success_redirect_uri: str
    error_redirect_uri: str
    status: AuthorizationFlowStatus
    grant_url: str
    connected_channel_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        connector_id = self.connector_id

        success_redirect_uri = self.success_redirect_uri

        error_redirect_uri = self.error_redirect_uri

        status = self.status.value

        grant_url = self.grant_url

        connected_channel_id = self.connected_channel_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "connector_id": connector_id,
                "success_redirect_uri": success_redirect_uri,
                "error_redirect_uri": error_redirect_uri,
                "status": status,
                "grant_url": grant_url,
            }
        )
        if connected_channel_id is not UNSET:
            field_dict["connected_channel_id"] = connected_channel_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        connector_id = d.pop("connector_id")

        success_redirect_uri = d.pop("success_redirect_uri")

        error_redirect_uri = d.pop("error_redirect_uri")

        status = AuthorizationFlowStatus(d.pop("status"))

        grant_url = d.pop("grant_url")

        connected_channel_id = d.pop("connected_channel_id", UNSET)

        authorization_flow = cls(
            id=id,
            connector_id=connector_id,
            success_redirect_uri=success_redirect_uri,
            error_redirect_uri=error_redirect_uri,
            status=status,
            grant_url=grant_url,
            connected_channel_id=connected_channel_id,
        )

        authorization_flow.additional_properties = d
        return authorization_flow

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
