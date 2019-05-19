from dateutil.parser import parse
from werkzeug.exceptions import BadRequest


class DatetimeConversionException(BadRequest):
    def __init__(self, message)


class MetricConversionException(BadRequest):
    def __init__(self, message):
        super().__init__(description = message)


def convert_to_datetime(value):
    try:
        value = parse(value)
    except (ValueError, OverflowError):
        raise DatetimeConversionException()
    return value


def convert_metric(value):
    try:
        value = float(value)
    except ValueError:
        raise MetricConversionException(value)
    return value