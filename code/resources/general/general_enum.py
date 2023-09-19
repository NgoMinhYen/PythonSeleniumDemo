from enum import Enum

    
class DateTimeFormat(Enum):
    ISO8601 = "%Y-%m-%dT%H:%M:%S.%fZ"
    FormatTime_V1 = "%Y-%m-%dT%H:%M:%SZ"


class APIScope(Enum):
    CLIENT_SCOPE = "CLIENT_SCOPE"
    SHARED_SCOPE = "SHARED_SCOPE"
    SERVER_SCOPE = "SERVER_SCOPE"
    INVALID_SCOPE = "abc!"


