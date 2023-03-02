from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateDriverResponse")


@attr.s(auto_attribs=True)
class CreateDriverResponse:
    """
    Attributes:
        driver_id (str):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.
    """

    driver_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        driver_id = self.driver_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "driverId": driver_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        driver_id = d.pop("driverId")

        create_driver_response = cls(
            driver_id=driver_id,
        )

        create_driver_response.additional_properties = d
        return create_driver_response

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
