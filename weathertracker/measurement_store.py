from   .measurement import Measurement
import weathertracker.utils.db as db
from   werkzeug.exceptions import abort


def add_measurement(date, metrics):
    dbstore = db.get_db()
    dbstore[date] = Measurement(date, metrics)


def get_measurement(date):
    return 


def query_measurements(start_date, end_date):
    # TODO:
    abort(501)
