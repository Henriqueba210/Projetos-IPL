from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.get_driver_response import GetDriverResponse


T = TypeVar("T", bound="ListDriversResponse")


@attr.s(auto_attribs=True)
class ListDriversResponse:
    """generic paged response

    Attributes:
        content (List['GetDriverResponse']): list of paged items
        total_results (int): total number of records Example: 50.
    """

    content: List["GetDriverResponse"]
    total_results: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = []
        for content_item_data in self.content:
            content_item = content_item_data.to_dict()

            content.append(content_item)

        total_results = self.total_results

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "totalResults": total_results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_driver_response import GetDriverResponse

        d = src_dict.copy()
        content = []
        _content = d.pop("content")
        for content_item_data in _content:
            content_item = GetDriverResponse.from_dict(content_item_data)

            content.append(content_item)

        total_results = d.pop("totalResults")

        list_drivers_response = cls(
            content=content,
            total_results=total_results,
        )

        list_drivers_response.additional_properties = d
        return list_drivers_response

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
