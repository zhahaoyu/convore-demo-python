from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbound_webhook import InboundWebhook


T = TypeVar("T", bound="SesChannel")


@_attrs_define
class SesChannel:
    """The specific ses channel information

    Attributes:
        sns_topic_arn (Union[Unset, str]): The SNS topic for SES to publish incoming message events to
        subscription_arn (Union[Unset, str]): The SNS subscription ARN that Convore uses to listen to the SNS topic
        inbound_webhook (Union[Unset, InboundWebhook]): The inbound webhook that this connector is associated with
    """

    sns_topic_arn: Union[Unset, str] = UNSET
    subscription_arn: Union[Unset, str] = UNSET
    inbound_webhook: Union[Unset, "InboundWebhook"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sns_topic_arn = self.sns_topic_arn

        subscription_arn = self.subscription_arn

        inbound_webhook: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inbound_webhook, Unset):
            inbound_webhook = self.inbound_webhook.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sns_topic_arn is not UNSET:
            field_dict["sns_topic_arn"] = sns_topic_arn
        if subscription_arn is not UNSET:
            field_dict["subscription_arn"] = subscription_arn
        if inbound_webhook is not UNSET:
            field_dict["inbound_webhook"] = inbound_webhook

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inbound_webhook import InboundWebhook

        d = src_dict.copy()
        sns_topic_arn = d.pop("sns_topic_arn", UNSET)

        subscription_arn = d.pop("subscription_arn", UNSET)

        _inbound_webhook = d.pop("inbound_webhook", UNSET)
        inbound_webhook: Union[Unset, InboundWebhook]
        if isinstance(_inbound_webhook, Unset):
            inbound_webhook = UNSET
        else:
            inbound_webhook = InboundWebhook.from_dict(_inbound_webhook)

        ses_channel = cls(
            sns_topic_arn=sns_topic_arn,
            subscription_arn=subscription_arn,
            inbound_webhook=inbound_webhook,
        )

        ses_channel.additional_properties = d
        return ses_channel

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
