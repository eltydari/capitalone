from collections import OrderedDict
from weathertracker.measurement_store import query_measurements

# Registered metrics will use metadata generated within get_stats
STATS = {
    # NOTE: We are rounding division to 10 digits to mitigate inaccuracies
    "average": lambda metadata: round(metadata["sum"]/metadata["count"], 10),
    "min": lambda metadata: metadata["min"],
    "max": lambda metadata: metadata["max"]
}
METADATA_TEMPLATE = {
    "sum": 0.0,
    "min": None,
    "max": None,
    "count": 0,
}
        
        
def validate_stats(stat_names):
    ret = []
    for name in stat_names:
        if name in STATS:
            ret.append(name)
    return ret
        
        
def validate_metric(metric_name, measurement):
    try:
        measurement.get_metric(metric_name)
        return True
    except KeyError:
        return False


def validate_metadata(data):
    return data["min"] is not None \
        and data["max"] is not None \
        and data["count"] > 0
    
        
class Stats(object):
    #The point o
    def __init__(self, metrics, start_date, end_date):
        self.measurements = query_measurements(start_date, end_date)
        self._aggregate_metrics(metrics)
        
    def _generate_metadata(self, metric_name):
        metadata = dict(METADATA_TEMPLATE)
        for measurement in self.measurements:
            if validate_metric(metric_name, measurement):
                metadata["count"] += 1
                metric = measurement.get_metric(metric_name)
                metadata["sum"] += metric
                if metadata["min"] is None:
                    metadata["min"] = metric
                elif metric < metadata["min"]:
                    metadata["min"] = metric
                if metadata["max"] is None:
                    metadata["max"] = metric
                elif metric > metadata["max"]:
                    metadata["max"] = metric
        if validate_metadata(metadata):
            self._metadata[metric_name] = metadata
        
    def _aggregate_metrics(self, metrics):
        self._metadata = OrderedDict()
        for metric_name in metrics:
            self._generate_metadata(metric_name)
        
    def get_stats(self, stats):
        ret = []
        for metric_name, metadata in self._metadata.items():
            for stat_name in stats:
                stat_func = STATS[stat_name]
                stat = {
                    "metric": metric_name,
                    "stat": stat_name,
                    "value": stat_func(metadata),
                }
                ret.append(stat)
        return ret


def get_stats(stats, metrics, from_datetime, to_datetime):
    stats = validate_stats(stats)
    stats_obj = Stats(metrics, from_datetime, to_datetime)
    return stats_obj.get_stats(stats)
