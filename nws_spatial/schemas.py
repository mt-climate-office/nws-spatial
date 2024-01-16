from enum import Enum


class Id(Enum):
    FORECAST = "forecast"
    COUNTY = "county"


class Type(Enum):
    LAND = "land"
    MARINE = "marine"
    FORECAST = "forecast"
    PUBLIC = "public"
    COASTAL = "coastal"
    OFFSHORE = "offshore"
    FIRE = "fire"
    COUNTY = "county"


class Status(Enum):
    ACTUAL = "actual"
    EXERCISE = "exercise"
    SYSTEM = "system"
    TEST = "test"
    DRAFT = "draft"


class MessageType(Enum):
    ALERT = "alert"
    UPDATE = "update"
    CANCEL = "cancel"


class RegionType(Enum):
    LAND = "land"
    MARINE = "marine"


class Urgency(Enum):
    IMMEDIATE = "Immediate"
    EXPECTED = "Expected"
    FUTURE = "Future"
    PAST = "Past"
    UNKNOWN = "Unknown"


class Severity(Enum):
    EXTREME = "Extreme"
    SEVERE = "Severe"
    MODERATE = "Moderate"
    MINOR = "Minor"
    UNKNOWN = "Unknown"


class Certainty(Enum):
    OBSERVED = "Observed"
    LIKELY = "Likely"
    POSSIBLE = "Possible"
    UNLIKELY = "Unlikely"
    UNKNOWN = "Unknown"
