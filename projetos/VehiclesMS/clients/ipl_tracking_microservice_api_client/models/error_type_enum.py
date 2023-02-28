from enum import Enum


class ErrorTypeEnum(str, Enum):
    PERSISTENCE = "PERSISTENCE"
    BUSINESS = "BUSINESS"
    COMMUNICATION = "COMMUNICATION"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
