from dateutil.parser import parse


class DatetimeConversionException(Exception):
    pass


def convert_to_datetime(value):
    try:
        value = parse(value)
    except (ValueError, OverflowError):
        raise DatetimeConversionException()
    return value


def convert_to_float(value):
    try:
        value = float(value)
    