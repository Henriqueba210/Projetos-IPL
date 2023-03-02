from enum import Enum


class EnumSensorType(str, Enum):
    RPM = "RPM"
    ODOMETER = "ODOMETER"
    SPEED = "SPEED"

    def __str__(self) -> str:
        return str(self.value)
