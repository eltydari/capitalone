from dateutil.parser import parse


class DatetimeConversionException(Exception):
    pass


class MetricConversionException(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value


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