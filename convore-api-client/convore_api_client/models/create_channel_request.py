from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_convore_mail_channel_params import CreateConvoreMailChannelParams
    from ..models.create_ses_channel_params import CreateSesChannelParams


T = TypeVar("T", bound="CreateChannelRequest")


@_attrs_define
class CreateChannelRequest:
    """
    Attributes:
        connector_id (str): Unique identifier for the channel's connector Example: conntr_01hcf9x766fqk8g7hz74363j9q.
        name (Union[Unset, str]): Name of the channel. Example: John's Gmail account.
        convore_mail (Union[Unset, CreateConvoreMailChannelParams]): Configuration used to create a channel for convore
            mail.
        ses (Union[Unset, CreateSesChannelParams]): Configuration used to create a channel for SES
    """

    connector_id: str
    name: Union[Unset, str] = UNSET
    convore_mail: Union[Unset, "CreateConvoreMailChannelParams"] = UNSET
    ses: Union[Unset, "CreateSesChannelParams"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connector_id = self.connector_id

        name = self.name

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
                "connector_id": connector_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if convore_mail is not UNSET:
            field_dict["convore_mail"] = convore_mail
        if ses is not UNSET:
            field_dict["ses"] = ses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_convore_mail_channel_params import CreateConvoreMailChannelParams
        from ..models.create_ses_channel_params import CreateSesChannelParams

        d = src_dict.copy()
        connector_id = d.pop("connector_id")

        name = d.pop("name", UNSET)

        _convore_mail = d.pop("convore_mail", UNSET)
        convore_mail: Union[Unset, CreateConvoreMailChannelParams]
        if isinstance(_convore_mail, Unset):
            convore_mail = UNSET
        else:
            convore_mail = CreateConvoreMailChannelParams.from_dict(_convore_mail)

        _ses = d.pop("ses", UNSET)
        ses: Union[Unset, CreateSesChannelParams]
        if isinstance(_ses, Unset):
            ses = UNSET
        else:
            ses = CreateSesChannelParams.from_dict(_ses)

        create_channel_request = cls(
            connector_id=connector_id,
            name=name,
            convore_mail=convore_mail,
            ses=ses,
        )

        create_channel_request.additional_properties = d
        return create_channel_request

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
