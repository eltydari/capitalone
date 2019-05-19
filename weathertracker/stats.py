from werkzeug.exceptions import abort
from weathertracker.measurement_store import query_measurements

METRICS = {
    "s"
}

def get_stats(stats, metrics, from_datetime, to_datetime):
   # TODO: 
   abort(501)
