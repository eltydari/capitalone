from dateutil.parser import parse
from werkzeug.exceptions import HTTPException


class DatetimeConversionException(HTTPException):
    self.code = 400
    self.description = ""
    #def __init__(self, message):
    #    super()
    #    self.code = 400
    #    self.description = message


def convert_to_datetime(value):
    try:
        value = parse(value)
    except (ValueError, OverflowError):
        raise DatetimeConversionException("Date input is invalid: {}".format(value))
    return value

