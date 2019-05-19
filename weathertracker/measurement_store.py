from   .measurement import Measurement
import weathertracker.utils.db as db
from   werkzeug.exceptions import abort


class EntryNotFoundException(Exception):
    pass


def add_measurement(measurement):
    dbstore = db.get_db()
    date = measurement["timestamp"]
    metrics = {k:v for k,v in measurment.items if k}
    dbstore[date] = Measurement(date, metrics)


def get_measurement(date):
    dbstore = db.get_db()
    measurement = dbstore.get(date)
    if not measurement:
        raise EntryNotFoundException
    ret = measurement.metrics
    ret['timestamp'] = measurment.timestamp
    return ret


def query_measurements(start_date, end_date):
    # TODO:
    abort(501)
