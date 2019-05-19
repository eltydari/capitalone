from werkzeug.exceptions import abort
from weathertracker.measurement_store import query_measurements

# Registered metrics will use metadata generated within get_stats
STATS = {
    "average": lambda metadata: metadata["sum"]/metadata["count"],
    "min": lambda metadata: metadata["min"],
    "max": lambda metadata: metadata["max"]
}
METADATA_TEMPLATE = {
    "sum": 0.0,
    "min": 0.0,
    "max": 0.0,
    "count": 0,
}


class InvalidStatException(Exception):
    def __init__(self, value):
        super().__init__()
        self.stat = value
        
        
class InvalidMetricException(Exception):
    def __init__(self):
        super().__init__()


def validate_stats(stat_names):
    for name in stat_names:
        if name not in STATS:
            raise InvalidStatException(name)
    return stat_names


def generate_metadata(metric, measurements):
    metadata = dict(METADATA_TEMPLATE)
    metadata["count"] = len(measurements)
    for measurement in measurements:
        metrics = 
    

def get_stats(stats, metrics, from_datetime, to_datetime):
    validate_stats(stats)
    measurements = query_measurements(from_datetime, to_datetime)
    
