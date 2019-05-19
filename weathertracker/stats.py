from werkzeug.exceptions import abort
from weathertracker.measurement_store import query_measurements

# Registered metrics will use metadata generated within get_stats
METRICS = {
    "average": lambda metadata: metadata["sum"]/metadata["count"],
    "min": lambda metadata: metadata["min"],
    "max": lambda metadata: metadata["max"]
}


class EntryNotFoundException(Exception):
    def __init__(self, value):
        super().__init__()
        self.entry = value


def validate_metrics(metric_names):
    for name in metric_names:
        if name not in METRICS:
            


def generate_metadata(measurements):
    pass


def get_stats(stats, metrics, from_datetime, to_datetime):
   measurements = query_measurements(from_datetime, to_datetime)
   
