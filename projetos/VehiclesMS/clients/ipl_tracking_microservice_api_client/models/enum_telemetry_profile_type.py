from enum import Enum


class EnumTelemetryProfileType(str, Enum):
    RPM = "RPM"
    ODOMETER = "ODOMETER"
    SPEED = "SPEED"

    def __str__(self) -> str:
        return str(self.value)
