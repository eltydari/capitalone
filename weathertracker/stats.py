from werkzeug.exceptions import abort
from weathertracker.measurement_store import query_measurements

METRICS = {
    "average": lambda metadata: metadata[sum]/metadata[count]
    "min": lambda m
}

def get_stats(stats, metrics, from_datetime, to_datetime):
   # TODO: 
   abort(501)
