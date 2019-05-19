from   .measurement import Measurement
import weathertracker.utils.db as db
from   werkzeug.exceptions import abort


class Exception(Exception):
    pass


def add_measurement(date, metrics):
    dbstore = db.get_db()
    dbstore[date] = Measurement(date, metrics)


def get_measurement(date):
    dbstore = db.get_db()
    return dbstore.get(date)


def query_measurements(start_date, end_date):
    # TODO:
    abort(501)
