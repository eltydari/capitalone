from dateutil.parser import parse


class DatetimeConversionException(Exception):
    pass

class MetricConversionException


def convert_to_datetime(value):
    try:
        value = parse(value)
    except (ValueError, OverflowError):
        raise DatetimeConversionException()
    return value


def convert_(value):
    try:
        value = float(value)
    except ValueError:
        raise 