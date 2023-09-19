from enum import Enum


class Dashboard(Enum):
    RPC_CUSTOM_CONTROL = "RPC Custom Control"
    RPC_MULTIPLE_DEVICES_DG800 = "DG800 RPC Multiple Devices"
    SEND_SMS_DG800 = "DG800 Send SMS"
    DEVICE_CONFIGURATION_DG800 = "DG800 Device configuration"
    DEVICE_DATA_AND_MAP = "Device Data And Map"
    DEVICE_DATA_AND_MAP_DG800 = "DG800 Device Data And Route Map"
    DEVICE_DATA_ROUTE_MAP_PROTOBUF = "Device Data Route Map ProtoBuf"
    RPC_MULTIPLE_DEVICES_DC400 = "DC400 RPC Multiple Devices"
    FMS_DASHBOARD_DC400 = "DC400 FMS Dashboard"
    HISTORIC_RPC_CALLS_DC400 = "DC400 Historic RPC Calls"
    CUSTOMER_SETUP_DASHBOARD = "Customer Setup Dashboard"
    RULE_ENGINE_STATISTICS = "Rule Engine Statistics"
    

class CloudMenu(Enum):
    ALL = "All"
    DG_800 = "DG800"
    DC_400 = "DC400"
    ADMIN = "Admin"
    HOME = "Home"
    ROLES = "Roles"
    CUSTOMERS_HIERARCHY = "Customers hierarchy"
    USER_GROUPS = "User groups"
    CUSTOMER_GROUPS = "Customer groups"
    ASSET_GROUPS = "Asset groups"
    DEVICE_GROUPS = "Device groups"
    ENTITY_VIEW_GROUPS = "Entity view groups"
    DASHBOARD_GROUPS = "Dashboard groups"
    SCHEDULER = "SCHEDULER"
    WHITE_LABELING = "White Labeling"
    AUDIT_LOGS = "Audit Logs"


class TimeseriesTableHeader(Enum): 
    CONVERTED_TIMESTAMP = "Timestamp"
    LATITUDE = "Latitude"
    LONGTITUDE = "Longitude"
    EVENT = "Event"
    SEQUENCE = "Seq"
    OBD_PROTOCOL = "Obd Protocol"
    VIN = "Vin"
    GPS_SPEED = "GPS Speed"
    VEHICLE_SPEED = "Vehicle Speed"
    HEADING = "Heading"
    SATELLITES = "Satellites"
    RSSI = "Rssi"
    ENGINE_ON_TIME = "Engine On Time"
    FUEL_LEVEL = "Fuel Level"
    RPM = "Rpm"
    MILEAGE = "Mileage"
    VEHICLE_BATTERY = "Vehicle Batt"
    BACKUP_BATTERY = "Backup Batt"
    TIMESTAMP = "timestamp"
    VALIDITY = "Validity"
    ELEVATION = "Elevation"
    OWTEMP1 = "Owtemp1"
    OWTEMP2 = "Owtemp2"
    PL = "Pl"
    
    
class TimeseriesTableColId(Enum): 
    DEVICE_TIMESTAMP = "Device timestamp"
    EVENT = "event"


class FilterType(Enum): 
    CONTAINS = "Contains"
    NOT_CONTAINS = "Not contains"
    EQUALS = "Equals"
    NOT_EQUAL = "Not equal"
    STARTS_WITH = "Starts with"
    ENDS_WITH = "Ends with"
    BLANK = "Blank"
    NOT_BLANK = "Not blank"


class FilterOperater(Enum):
    OR = "OR"
    AND = "AND"


class EditTimeWindow(Enum):
    UPDATE_BUTTON = "Update"
    CANCEL_BUTTON = "Cancel"
    REALTIME_TAB = "Realtime"
    HISTORY_TAB = "History"
    ADVANCE_DAYS_FIELD = "Days"
    ADVANCE_HOURS_FIELD = "Hours"
    ADVANCE_MINUTES_FIELD = "Minutes"
    ADVANCE_SECONDS_FIELD = "Seconds"
    LAST = "Last"
    TIME_PERIOD = "Time period"

    
class ConfirmDialog(Enum):
    YES = "Yes"
    NO = "No" 
    
    
class DG800ConfigurationName(Enum):
    APNLIST = "apnlist"
    HARSHBRAKE = "harshbrake"
    HARSHACCEL = "harshaccel"
    HARSHTURN = "harshturn"
    HEADING = "heading"
    HEARTBEAT = "heartbeat"
    HIGHGFORCE = "highgforce"
    IMU = "imu"
    INTERVAL = "interval"
    PARKTIMER = "parktimer"
    PERIODREBOOT = "periodreboot"
    SPEEDALARM = "speedalarm"
    SLEEPWAIT = "sleepwait"
    
    
class DC400ConfigurationName(Enum):
    INTERNAL_LED_ENABLE = "Internal LED Enable"
    FCWS = "FCWS"
    DMS_TRIGGER_SPEED = "DMS trigger speed"
    DMS_DEBOUNCE_TIMER = "DMS-debounce-timer"
    DMS_DETECTION_TIMER = "DMS-detection-timer"
    DMS_FATIGUE_TRIGGER_TIMER = "DMS-fatigue-trigger-timer"
    FCWS_SENSITIVITY = "FCWS Sensitivity"
    FCWS_TAILGATING_DEBOUNCE_TIMER = "FCWS-tailgating-debounce-timer"
    LDWS_L = "LDWS L"
    LDWS_R = "LDWS R"
    LDWS_ENABLE = "LDWS enable"
    SPEAKER_VOLUME = "Speaker Volume"
    
       
class DC400RPCMethod(Enum):
    VERSION = "version"
    FW_OTA = "fw-ota"
    REBOOT = "reboot"
    CONFIG_SET = "config-set"
    CONFIG_GET = "config-get"
    
    
class ConfigurationValue(Enum):
    TRUE = "True"
    FALSE = "False"
    
    
class DC400EventPriority(Enum):
    HIGH = "High Priority (on)"
    NORMAL = "High Priority (off)"
    
class EventPriority(Enum):
    HIGH = "high"
    NORMAL = "normal"
    

class RGBColor(Enum):
    ORANGE = "rgb(255, 214, 135)"
    BLUE = "rgb(150, 225, 255)"
    PINK = "rgb(255, 236, 236)"

