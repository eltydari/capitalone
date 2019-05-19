from   .measurement import Measurement
import weathertracker.utils.db as db
from   weathertracker.utils.conversion import convert_to_datetime
from   werkzeug.exceptions import abort


class EntryNotFoundException(Exception):
    pass


def add_measurement(measurement):
    dbstore = db.get_db()
    date_str = measurement["timestamp"]
    date = convert_to_datetime(date_str)
    metrics = {k:v for k,v in measurement.items() if k != "timestamp"}
    dbstore[date] = Measurement(date_str, metrics)


def get_measurement(date):
    dbstore = db.get_db()
    measurement = dbstore.get(date)
    if not measurement:
        raise EntryNotFoundException
    ret = measurement.metrics
    ret['timestamp'] = measurement.timestamp
    return ret


def query_measurements(start_date, end_date):
    # TODO:
    abort(501)
