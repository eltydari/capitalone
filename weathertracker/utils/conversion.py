from dateutil.parser import parse
from werkzeug.exceptions import HTTPException


class DatetimeConversionException(HTTPException):
    code = 400



def convert_to_datetime(value):
    try:
        value = parse(value)
    except (ValueError, OverflowError):
        raise DatetimeConversionException()
    return value

