from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.error_type_enum import ErrorTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponse")


@attr.s(auto_attribs=True)
class ErrorResponse:
    """
    Attributes:
        code (Union[Unset, str]): Application error code Example: CST0001.
        type (Union[Unset, ErrorTypeEnum]): Error Type
        message (Union[Unset, str]): Short error explanation Example: Unauthorized.
        details (Union[Unset, str]): Short error detail Example: Parameter X has invalid value.
    """

    code: Union[Unset, str] = UNSET
    type: Union[Unset, ErrorTypeEnum] = UNSET
    message: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        message = self.message
        details = self.details

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if type is not UNSET:
            field_dict["type"] = type
        if message is not UNSET:
            field_dict["message"] = message
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ErrorTypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ErrorTypeEnum(_type)

        message = d.pop("message", UNSET)

        details = d.pop("details", UNSET)

        error_response = cls(
            code=code,
            type=type,
            message=message,
            details=details,
        )

        error_response.additional_properties = d
        return error_response

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
