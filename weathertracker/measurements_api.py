from   flask import request, jsonify
from   flask.views import MethodView
from   werkzeug.wrappers import Response
from   werkzeug.exceptions import BadRequest, NotFound
import weathertracker.measurement_store as mdb
from   weathertracker.utils.conversion import (
    convert_to_datetime,
    DatetimeConversionException,
    convert_metric,
    MetricConversionException,
)


def parse_timestamp(timestamp):
    try:
        timestamp = convert_to_datetime(timestamp)
    except DatetimeConversionException:
        raise BadRequest(description = "Timestamp input is invalid: {}".format(timestamp))
    return timestamp
    

def process_measurement(pairs):
    try:
        for key, value in pairs.items():
            if key == "timestamp":
                continue
            if not isinstance(key, str):
                raise BadRequest(description = "Input metric key is not a string: {}".format(key))
            pairs[key] = convert_metric(value)
    except MetricConversionException as e:
        raise BadRequest(description = "Input metric value is not a float: {}".format(e.value))
    except BadRequest:
        pass
    return pairs


class MeasurementsAPI(MethodView):

    # features/01-measurements/01-add-measurement.feature
    def post(self):
        
        req = request.get_json()
        
        timestamp = req.get("timestamp")
        if not timestamp:
            raise BadRequest(description = "Input timestamp was expected but not provided.")
        parse_timestamp(timestamp) #Do validation
        
        process_measurement(req)
        mdb.add_measurement(req)
        
        resp = Response("Success!", status=201)
        resp.headers.add("Location", "/measurements/{}".format(timestamp))
        return resp

    # features/01-measurements/02-get-measurement.feature
    def get(self, timestamp):

        timestamp = parse_timestamp(timestamp)
        
        try:
            measurement = mdb.get_measurement(timestamp)
        except mdb.EntryNotFoundException as e:
            raise NotFound("Entry was not found in database: {}".format(e.entry))
            
        return jsonify(measurement)
