from   .measurement import Measurement
import weathertracker.utils.db as db
from   werkzeug.exceptions import abort


def add_measurement(date, metrics):
    dbstore = db.get_db()
    dbstore[date] = Measurement(d)


def get_measurement(date):
    # TODO:
    abort(501)


def query_measurements(start_date, end_date):
    # TODO:
    abort(501)
