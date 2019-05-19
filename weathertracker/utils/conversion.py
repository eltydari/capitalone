from dateutil.parser import parse


class DatetimeConversionException(ConversionException):
    pass


class MetricConversionException(Exception):
    pass


def convert_to_datetime(value):
    try:
        value = parse(value)
    except (ValueError, OverflowError):
        raise DatetimeConversionException(value)
    return value


def convert_metric(value):
    try:
        value = float(value)
    except ValueError:
        raise MetricConversionException(value)
    return value