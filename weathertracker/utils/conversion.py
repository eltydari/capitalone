from dateutil.parser import parse


class ConversionException(Exception):
    def __init__(self, value):
        super.__init__()
        self.value = value


class DatetimeConversionException(ConversionException):
    pass


class MetricConversionException(Exception):
    def __init__(self, message):
        super.__init__()
        self.value = value


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