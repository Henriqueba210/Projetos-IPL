from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDriverResponse")


@attr.s(auto_attribs=True)
class GetDriverResponse:
    """
    Attributes:
        driver_id (str):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.
        name (str): Complete Driver name Example: Foo bar.
        phone (str): Telephone number Example: 351912000111.
        mail (str): E-mail address Example: foo@bar.com.
        customer_id (Union[Unset, str]):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.
    """

    driver_id: str
    name: str
    phone: str
    mail: str
    customer_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        driver_id = self.driver_id
        name = self.name
        phone = self.phone
        mail = self.mail
        customer_id = self.customer_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "driverId": driver_id,
                "name": name,
                "phone": phone,
                "mail": mail,
            }
        )
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        driver_id = d.pop("driverId")

        name = d.pop("name")

        phone = d.pop("phone")

        mail = d.pop("mail")

        customer_id = d.pop("customerId", UNSET)

        get_driver_response = cls(
            driver_id=driver_id,
            name=name,
            phone=phone,
            mail=mail,
            customer_id=customer_id,
        )

        get_driver_response.additional_properties = d
        return get_driver_response

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
