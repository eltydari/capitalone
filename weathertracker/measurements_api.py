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


class MeasurementsAPI(MethodView):

    # features/01-measurements/01-add-measurement.feature
    def post(self):
        
        req = request.get_json()
        
        timestamp = req.get("timestamp")
        if not timestamp:
            raise BadRequest(description = "Timestamp was expected in the post request but not provided")
        timestamp = parse_timestamp(timestamp)
        
        try:
            metrics = {k:convert_metric(v) for k,v in req.items() if k != "timestamp"}
        except MetricConversionException:
            raise BadRequest(description = "Metric is not a float: <{}> with value <{}>".format(k))
            
        mdb.add_measurement(timestamp, metrics)
        
        resp = Response("Success!", status=201)
        resp.headers.add("Location", "/measurements/{}".format(timestamp))
        return resp

    # features/01-measurements/02-get-measurement.feature
    def get(self, timestamp):

        timestamp = parse_timestamp(timestamp)

        # TODO:
        abort(501)
