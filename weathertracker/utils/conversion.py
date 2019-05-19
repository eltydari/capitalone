from dateutil.parser import parse
from werkzeug.exceptions import HTTPException


class DatetimeConversionException(HTTPException):
    def __init__(self, message):
        super()
        self.description = message


def convert_to_datetime(value):
    try:
        value = parse(value)
    except (ValueError, OverflowError):
        raise DatetimeConversionException("Date input is invalid: {}".format(value))
    return value

