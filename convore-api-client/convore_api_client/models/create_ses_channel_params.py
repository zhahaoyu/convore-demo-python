from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSesChannelParams")


@_attrs_define
class CreateSesChannelParams:
    """Configuration used to create a channel for SES

    Attributes:
        sns_topic_arn (Union[Unset, str]): The SNS topic for SES to publish incoming message events to.
    """

    sns_topic_arn: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sns_topic_arn = self.sns_topic_arn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sns_topic_arn is not UNSET:
            field_dict["sns_topic_arn"] = sns_topic_arn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sns_topic_arn = d.pop("sns_topic_arn", UNSET)

        create_ses_channel_params = cls(
            sns_topic_arn=sns_topic_arn,
        )

        create_ses_channel_params.additional_properties = d
        return create_ses_channel_params

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
