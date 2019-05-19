from   .measurement import Measurement
import weathertracker.utils.db as db
from   werkzeug.exceptions import abort


class EntryNotFoundException(Exception):
    pass


def add_measurement(date, measuremen):
    dbstore = db.get_db()
    dbstore[date] = Measurement(date, metrics)


def get_measurement(date):
    dbstore = db.get_db()
    measurement = dbstore.get(date)
    if not measurement:
        raise EntryNotFoundException
    return measurement


def query_measurements(start_date, end_date):
    # TODO:
    abort(501)
