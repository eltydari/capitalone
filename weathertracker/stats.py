from werkzeug.exceptions import abort
from weathertracker.measurement_store import query_measurements

METRICS = {
    "min": lambda metadata
}

def get_stats(stats, metrics, from_datetime, to_datetime):
   # TODO: 
   abort(501)
