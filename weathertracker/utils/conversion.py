from dateutil.parser import parse
from werkzeug.exceptions import BadRequest

class DatetimeConversionException(Exception):
    pass


def convert_to_datetime(value):
    try:
        value = parse(value)
    except (ValueError, OverflowError):
        raise DatetimeConversionException()
    return value

