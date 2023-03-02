from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDriverRequest")


@attr.s(auto_attribs=True)
class UpdateDriverRequest:
    """
    Attributes:
        name (Union[Unset, str]): Complete Driver name Example: Foo bar.
        customer_id (Union[Unset, str]):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.
        phone (Union[Unset, str]): Telephone number Example: 351912000111.
        mail (Union[Unset, str]): E-mail address Example: foo@bar.com.
    """

    name: Union[Unset, str] = UNSET
    customer_id: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    mail: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        customer_id = self.customer_id
        phone = self.phone
        mail = self.mail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if mail is not UNSET:
            field_dict["mail"] = mail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        customer_id = d.pop("customerId", UNSET)

        phone = d.pop("phone", UNSET)

        mail = d.pop("mail", UNSET)

        update_driver_request = cls(
            name=name,
            customer_id=customer_id,
            phone=phone,
            mail=mail,
        )

        update_driver_request.additional_properties = d
        return update_driver_request

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
