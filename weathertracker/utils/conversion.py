from dateutil.parser import parse


class DatetimeConversionException(Exception):
    pass


class MetricConversionException(Exception):
    


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
        raise MetricConversionException()
    return value