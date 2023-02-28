from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateTelemetryProfileResponse")


@attr.s(auto_attribs=True)
class CreateTelemetryProfileResponse:
    """
    Attributes:
        telemetryprofile_id (str):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.
    """

    telemetryprofile_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        telemetryprofile_id = self.telemetryprofile_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "telemetryprofileId": telemetryprofile_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        telemetryprofile_id = d.pop("telemetryprofileId")

        create_telemetry_profile_response = cls(
            telemetryprofile_id=telemetryprofile_id,
        )

        create_telemetry_profile_response.additional_properties = d
        return create_telemetry_profile_response

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
