from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact import Contact


T = TypeVar("T", bound="PageContact")


@_attrs_define
class PageContact:
    """
    Attributes:
        data (List['Contact']):
        next_cursor (Union[Unset, str]):
        total_count (Union[Unset, int]): The total number of objects that match the query
    """

    data: List["Contact"]
    next_cursor: Union[Unset, str] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_cursor = self.next_cursor

        total_count = self.total_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact import Contact

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Contact.from_dict(data_item_data)

            data.append(data_item)

        next_cursor = d.pop("next_cursor", UNSET)

        total_count = d.pop("total_count", UNSET)

        page_contact = cls(
            data=data,
            next_cursor=next_cursor,
            total_count=total_count,
        )

        page_contact.additional_properties = d
        return page_contact

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
