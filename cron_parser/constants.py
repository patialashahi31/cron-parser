MINUTE = "minute"
HOUR = "hour"
DAY_OF_MONTH = "day of month"
MONTH = "month"
DAY_OF_WEEK = "day of week"

# Field names
FIELD_NAMES = [MINUTE, HOUR, DAY_OF_MONTH, MONTH, DAY_OF_WEEK]

# Allowed value ranges
FIELD_RANGES = {
    MINUTE: (0, 59),
    HOUR: (0, 23),
    DAY_OF_MONTH: (1, 31),
    MONTH: (1, 12),
    DAY_OF_WEEK: (0, 6),
}
