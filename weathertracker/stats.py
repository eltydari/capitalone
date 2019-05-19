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
    "min": None,
    "max": None,
    "count": 0,
}


class InvalidStatException(Exception):
    def __init__(self, value):
        super().__init__()
        self.stat = value
        
        
class InvalidMetricException(Exception):
    def __init__(self, value, timestamp):
        super().__init__()
        self.metric = metric
        self.timestamp = timestamp
        
        
def validate_stats(stat_names):
    for name in stat_names:
        if name not in STATS:
            raise InvalidStatException(name)
    return stat_names
        
        
def validate_metric(metric_name, measurement):
    try:
        metric = measurement.get_metric(metric_name)
    except KeyError:
        raise InvalidMetricException(metric_name, measurement["timestamp"])
    return measurement[metric]
        
        
class Stats(object):
    def __init__(self, start_date, end_date):
        self.measurements = query_measurements(from_datetime, to_datetime)
        self._metadata = {}
        
    def _generate_metadata(self, metric_name):
        metadata = dict(METADATA_TEMPLATE)
        metadata["count"] = len(self.measurements)
        for measurement in self.measurements:
            metric = validate_metric(metric_name, measurement)
            metadata["sum"] += metric
            if metadata["min"] is None:
                metadata["min"] = metric
            elif metric < metadata["min"]:
                metadata["min"] = metric
            if metadata["max"] is None:
                metadata["max"] = metric
            elif metric > metadata["max"]:
                metadata["max"] = metric
         self._metadata[metric_name] = metadata
        

def get_stats(stats, metrics, from_datetime, to_datetime):
    validate_stats(stats)
    measurements = query_measurements(from_datetime, to_datetime)
    for metric_name in metrics:
        metric_data = generate_metadata(metric_name, measurements)
        
