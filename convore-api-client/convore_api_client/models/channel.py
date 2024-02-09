import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.channel_status import ChannelStatus
from ..models.provider_type import ProviderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_address import ChannelAddress
    from ..models.convore_mail_channel import ConvoreMailChannel
    from ..models.ses_channel import SesChannel


T = TypeVar("T", bound="Channel")


@_attrs_define
class Channel:
    """
    Attributes:
        id (str): Unique identifier for the channel Example: chnnl_01hcf9x766fqk8g7hz74363j9q.
        connector_id (str): Unique identifier for the channel's connector Example: conntr_01hcf9x766fqk8g7hz74363j9q.
        provider (ProviderType): The provider type
        name (str): Name of the channel Example: John's Gmail account.
        addresses (List['ChannelAddress']): A collection of communication addresses associated with the channel. These
            addresses are used for sending and receiving messages, ensuring proper routing and delivery of content. Each
            address specifies a unique handle, such as an email or a phone number, along with associated details like the
            participant's name and role.
        status (ChannelStatus): The status of the channel.
        created_at (datetime.datetime): The ISO 8601 time at which the Channel was created.
        convore_mail (Union[Unset, ConvoreMailChannel]): The specific convore mail channel information
        ses (Union[Unset, SesChannel]): The specific ses channel information
    """

    id: str
    connector_id: str
    provider: ProviderType
    name: str
    addresses: List["ChannelAddress"]
    status: ChannelStatus
    created_at: datetime.datetime
    convore_mail: Union[Unset, "ConvoreMailChannel"] = UNSET
    ses: Union[Unset, "SesChannel"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        connector_id = self.connector_id

        provider = self.provider.value

        name = self.name

        addresses = []
        for addresses_item_data in self.addresses:
            addresses_item = addresses_item_data.to_dict()
            addresses.append(addresses_item)

        status = self.status.value

        created_at = self.created_at.isoformat()

        convore_mail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.convore_mail, Unset):
            convore_mail = self.convore_mail.to_dict()

        ses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ses, Unset):
            ses = self.ses.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "connector_id": connector_id,
                "provider": provider,
                "name": name,
                "addresses": addresses,
                "status": status,
                "created_at": created_at,
            }
        )
        if convore_mail is not UNSET:
            field_dict["convore_mail"] = convore_mail
        if ses is not UNSET:
            field_dict["ses"] = ses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.channel_address import ChannelAddress
        from ..models.convore_mail_channel import ConvoreMailChannel
        from ..models.ses_channel import SesChannel

        d = src_dict.copy()
        id = d.pop("id")

        connector_id = d.pop("connector_id")

        provider = ProviderType(d.pop("provider"))

        name = d.pop("name")

        addresses = []
        _addresses = d.pop("addresses")
        for addresses_item_data in _addresses:
            addresses_item = ChannelAddress.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        status = ChannelStatus(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        _convore_mail = d.pop("convore_mail", UNSET)
        convore_mail: Union[Unset, ConvoreMailChannel]
        if isinstance(_convore_mail, Unset):
            convore_mail = UNSET
        else:
            convore_mail = ConvoreMailChannel.from_dict(_convore_mail)

        _ses = d.pop("ses", UNSET)
        ses: Union[Unset, SesChannel]
        if isinstance(_ses, Unset):
            ses = UNSET
        else:
            ses = SesChannel.from_dict(_ses)

        channel = cls(
            id=id,
            connector_id=connector_id,
            provider=provider,
            name=name,
            addresses=addresses,
            status=status,
            created_at=created_at,
            convore_mail=convore_mail,
            ses=ses,
        )

        channel.additional_properties = d
        return channel

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
