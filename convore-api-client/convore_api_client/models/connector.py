import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.provider_type import ProviderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gmail_connector import GmailConnector
    from ..models.ses_connector import SesConnector


T = TypeVar("T", bound="Connector")


@_attrs_define
class Connector:
    """
    Attributes:
        id (str): Unique identifier of the connector. Example: conntr_01hcf9x766fqk8g7hz74363j9q.
        provider (ProviderType): The provider type
        name (str): Name of the connector Example: Acme Corp's Gmail OAuth App.
        created_at (datetime.datetime): The ISO 8601 time at which the Connector was created.
        gmail (Union[Unset, GmailConnector]): Gmail configuration
        ses (Union[Unset, SesConnector]): SES configuration
    """

    id: str
    provider: ProviderType
    name: str
    created_at: datetime.datetime
    gmail: Union[Unset, "GmailConnector"] = UNSET
    ses: Union[Unset, "SesConnector"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        provider = self.provider.value

        name = self.name

        created_at = self.created_at.isoformat()

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
                "id": id,
                "provider": provider,
                "name": name,
                "created_at": created_at,
            }
        )
        if gmail is not UNSET:
            field_dict["gmail"] = gmail
        if ses is not UNSET:
            field_dict["ses"] = ses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gmail_connector import GmailConnector
        from ..models.ses_connector import SesConnector

        d = src_dict.copy()
        id = d.pop("id")

        provider = ProviderType(d.pop("provider"))

        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        _gmail = d.pop("gmail", UNSET)
        gmail: Union[Unset, GmailConnector]
        if isinstance(_gmail, Unset):
            gmail = UNSET
        else:
            gmail = GmailConnector.from_dict(_gmail)

        _ses = d.pop("ses", UNSET)
        ses: Union[Unset, SesConnector]
        if isinstance(_ses, Unset):
            ses = UNSET
        else:
            ses = SesConnector.from_dict(_ses)

        connector = cls(
            id=id,
            provider=provider,
            name=name,
            created_at=created_at,
            gmail=gmail,
            ses=ses,
        )

        connector.additional_properties = d
        return connector

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
