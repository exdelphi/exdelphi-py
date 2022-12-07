from datetime import datetime, timezone


def datetime_to_int(datetime_object: datetime) -> int:
    """Returns Unix timestamp (in seconds) for given datetime"""
    datetime_object = datetime_object.timestamp()
    return int(datetime_object)


def datetime_string_to_int(datetime_string: str, format_string: str) -> int:
    """Returns Unix timestamp (in seconds) for given datetime UTC string with specified formatting"""
    dt = datetime.strptime(datetime_string, format_string).replace(tzinfo=timezone.utc)
    return datetime_to_int(dt)


def int_to_datetime(unix_timestamp: int) -> datetime:
    """Returns datetime object created from given unix timestamp"""
    return datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
