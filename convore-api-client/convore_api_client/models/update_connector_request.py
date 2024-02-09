from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_gmail_connector_params import UpdateGmailConnectorParams
    from ..models.update_ses_connector_params import UpdateSesConnectorParams


T = TypeVar("T", bound="UpdateConnectorRequest")


@_attrs_define
class UpdateConnectorRequest:
    """
    Attributes:
        name (Union[Unset, str]): Name of the connector Example: Acme Corp's Gmail OAuth App.
        gmail (Union[Unset, UpdateGmailConnectorParams]): Gmail configuration
        ses (Union[Unset, UpdateSesConnectorParams]): SES configuration. Only the non-null fields are set
    """

    name: Union[Unset, str] = UNSET
    gmail: Union[Unset, "UpdateGmailConnectorParams"] = UNSET
    ses: Union[Unset, "UpdateSesConnectorParams"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        gmail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gmail, Unset):
            gmail = self.gmail.to_dict()

        ses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ses, Unset):
            ses = self.ses.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if gmail is not UNSET:
            field_dict["gmail"] = gmail
        if ses is not UNSET:
            field_dict["ses"] = ses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_gmail_connector_params import UpdateGmailConnectorParams
        from ..models.update_ses_connector_params import UpdateSesConnectorParams

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _gmail = d.pop("gmail", UNSET)
        gmail: Union[Unset, UpdateGmailConnectorParams]
        if isinstance(_gmail, Unset):
            gmail = UNSET
        else:
            gmail = UpdateGmailConnectorParams.from_dict(_gmail)

        _ses = d.pop("ses", UNSET)
        ses: Union[Unset, UpdateSesConnectorParams]
        if isinstance(_ses, Unset):
            ses = UNSET
        else:
            ses = UpdateSesConnectorParams.from_dict(_ses)

        update_connector_request = cls(
            name=name,
            gmail=gmail,
            ses=ses,
        )

        update_connector_request.additional_properties = d
        return update_connector_request

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
