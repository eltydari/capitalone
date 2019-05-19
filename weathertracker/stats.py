from werkzeug.exceptions import abort
from weathertracker.measurement_store import query_measurements

METRICS = {
    "avera": lambda metadata: metadata[sum]/metadata[count]
    ""
}

def get_stats(stats, metrics, from_datetime, to_datetime):
   # TODO: 
   abort(501)
