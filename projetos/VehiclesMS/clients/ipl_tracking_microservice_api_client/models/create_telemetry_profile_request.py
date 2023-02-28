from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTelemetryProfileRequest")


@attr.s(auto_attribs=True)
class CreateTelemetryProfileRequest:
    """
    Attributes:
        name (str): Complete TelemetryProfile name Example: Foo bar.
        sensors (Union[Unset, List[str]]): unique identifier of the sensors in the database
    """

    name: str
    sensors: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        sensors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sensors, Unset):
            sensors = self.sensors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if sensors is not UNSET:
            field_dict["sensors"] = sensors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        sensors = cast(List[str], d.pop("sensors", UNSET))

        create_telemetry_profile_request = cls(
            name=name,
            sensors=sensors,
        )

        create_telemetry_profile_request.additional_properties = d
        return create_telemetry_profile_request

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
