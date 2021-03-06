from enum import IntEnum


class EventCodes(IntEnum):
    LE_EVENTS = 0x3e
    VENDOR_SPECIFIC_EVENT = 0xFF
    DISCONNECTION_COMPLETE = 0x05
    ENCRYPTION_CHANGE = 0x08
    READ_REMOTE_VERSION_INFORMATION_COMPLETE = 0x0C
    HCI_COMMAND_COMPLETE = 0x0E
    COMMAND_STATUS = 0x0F
    HARDWARE_ERROR = 0x10
    NUMBER_OF_COMPLETED_PACKETS = 0x13
    DATA_BUFFER_OVERFLOW = 0x1A
    ENCRYPTION_KEY_REFRESH_COMPLETE = 0x30
    AUTHENTICATED_PAYLOAD_TIMEOUT_EXPIRED = 0x57
