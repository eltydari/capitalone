from   .measurement import Measurement
import weathertracker.utils.db as db
from   weathertracker.utils.conversion import convert_to_datetime
from   werkzeug.exceptions import abort


class EntryNotFoundException(Exception):
    pass


def add_measurement(measurement):
    dbstore = db.get_db()
    dateS
    date = convert_to_datetime(measurement["timestamp"])
    metrics = {k:v for k,v in measurement.items() if k != "timestamp"}
    dbstore[date] = Measurement(measurement["timestamp"], metrics)


def get_measurement(date):
    print(date)
    dbstore = db.get_db()
    print(dbstore)
    measurement = dbstore.get(date)
    if not measurement:
        raise EntryNotFoundException
    ret = measurement.metrics
    ret['timestamp'] = measurement.timestamp
    return ret


def query_measurements(start_date, end_date):
    # TODO:
    abort(501)
