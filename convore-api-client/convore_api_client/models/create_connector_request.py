from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_type import ProviderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_gmail_connector_params import CreateGmailConnectorParams
    from ..models.create_ses_connector_params import CreateSesConnectorParams


T = TypeVar("T", bound="CreateConnectorRequest")


@_attrs_define
class CreateConnectorRequest:
    """
    Attributes:
        provider (ProviderType): The provider type
        name (Union[Unset, str]): Name of the connector Example: Acme Corp's Gmail OAuth App.
        gmail (Union[Unset, CreateGmailConnectorParams]): Gmail configuration
        ses (Union[Unset, CreateSesConnectorParams]): SES configuration
    """

    provider: ProviderType
    name: Union[Unset, str] = UNSET
    gmail: Union[Unset, "CreateGmailConnectorParams"] = UNSET
    ses: Union[Unset, "CreateSesConnectorParams"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider = self.provider.value

        name = self.name

        gmail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gmail, Unset):
            gmail = self.gmail.to_dict()

        ses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ses, Unset):
            ses = self.ses.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if gmail is not UNSET:
            field_dict["gmail"] = gmail
        if ses is not UNSET:
            field_dict["ses"] = ses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_gmail_connector_params import CreateGmailConnectorParams
        from ..models.create_ses_connector_params import CreateSesConnectorParams

        d = src_dict.copy()
        provider = ProviderType(d.pop("provider"))

        name = d.pop("name", UNSET)

        _gmail = d.pop("gmail", UNSET)
        gmail: Union[Unset, CreateGmailConnectorParams]
        if isinstance(_gmail, Unset):
            gmail = UNSET
        else:
            gmail = CreateGmailConnectorParams.from_dict(_gmail)

        _ses = d.pop("ses", UNSET)
        ses: Union[Unset, CreateSesConnectorParams]
        if isinstance(_ses, Unset):
            ses = UNSET
        else:
            ses = CreateSesConnectorParams.from_dict(_ses)

        create_connector_request = cls(
            provider=provider,
            name=name,
            gmail=gmail,
            ses=ses,
        )

        create_connector_request.additional_properties = d
        return create_connector_request

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
