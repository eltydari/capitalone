from   flask import request, jsonify
from   flask.views import MethodView
from   werkzeug.wrappers import Response
from   werkzeug.exceptions import abort, BadRequest, NotFound
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
    

def process_measurement(req_json):
    try:
        for key, value in req_json.items():
            if key == "timestamp":
                continue
            req_json[key] = convert_metric(value)
    except MetricConversionException as e:
        raise BadRequest(description = "Input metric value is not a float: {}".format(e.value))
    return req_json
    
    
def stringify(collection):
    # Main purpose is to turn '0.0' into '0'
    for key, value in ret_json.items():
        if value == 0:
            value = 0
        ret_json[key] = str(value)
    return ret_json


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
        except mdb.EntryNotFoundException:
            raise NotFound("Entry was not found in database.")
            
        return jsonify(measurement)
