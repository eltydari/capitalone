from werkzeug.exceptions import abort
from weathertracker.measurement_store import query_measurements

METRICS = {
    "average": lambda metadata: metadata[sum]/metadata[count],
    "min": lambda metadata: metadata[min],
    "max": lambda metadata: metadata[max]
}

def get_stats(stats, metrics, from_datetime, to_datetime):
   # TODO: 
   abort(501)
