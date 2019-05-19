from   flask import request, jsonify
from   flask.views import MethodView
from   werkzeug.wrappers import Response
from   werkzeug.exceptions import abort, BadRequest
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
    for key, value in req_json.items():
        if k == "timestamp":
            continue
        
    
    try:
        ret = {k:convert_metric(v) for k,v in req_json.items() if k != "timestamp"}
    except MetricConversionException as e:
        raise BadRequest(description = "Input metric value is not a float: {}".format(e.value))
    return ret


class MeasurementsAPI(MethodView):

    # features/01-measurements/01-add-measurement.feature
    def post(self):
        
        req = request.get_json()
        
        timestamp = req.get("timestamp")
        if not timestamp:
            raise BadRequest(description = "Input timestamp was expected but not provided.")
        timestamp = parse_timestamp(timestamp)
        
        mdb.add_measurement(req)
        
        resp = Response("Success!", status=201)
        resp.headers.add("Location", "/measurements/{}".format(timestamp))
        return resp

    # features/01-measurements/02-get-measurement.feature
    def get(self, timestamp):

        timestamp = parse_timestamp(timestamp)

        metrics = get_measurement(timestamp)
        # TODO:
        abort(501)
