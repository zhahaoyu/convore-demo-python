from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_status import ChannelStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_convore_mail_channel_params import UpdateConvoreMailChannelParams


T = TypeVar("T", bound="UpdateChannelRequest")


@_attrs_define
class UpdateChannelRequest:
    """
    Attributes:
        name (Union[Unset, str]): Name of the channel Example: John's Gmail account.
        status (Union[Unset, ChannelStatus]): The status of the channel.
        convore_mail (Union[Unset, UpdateConvoreMailChannelParams]):
    """

    name: Union[Unset, str] = UNSET
    status: Union[Unset, ChannelStatus] = UNSET
    convore_mail: Union[Unset, "UpdateConvoreMailChannelParams"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        convore_mail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.convore_mail, Unset):
            convore_mail = self.convore_mail.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if convore_mail is not UNSET:
            field_dict["convore_mail"] = convore_mail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_convore_mail_channel_params import UpdateConvoreMailChannelParams

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ChannelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ChannelStatus(_status)

        _convore_mail = d.pop("convore_mail", UNSET)
        convore_mail: Union[Unset, UpdateConvoreMailChannelParams]
        if isinstance(_convore_mail, Unset):
            convore_mail = UNSET
        else:
            convore_mail = UpdateConvoreMailChannelParams.from_dict(_convore_mail)

        update_channel_request = cls(
            name=name,
            status=status,
            convore_mail=convore_mail,
        )

        update_channel_request.additional_properties = d
        return update_channel_request

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
