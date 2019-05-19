from flask import request, jsonify
from flask.views import MethodView
from werkzeug.exceptions import abort, BadRequest
from weathertracker.utils.conversion import (
    convert_to_datetime,
    DatetimeConversionException,
    convert_metric,
    MetricConversionException,
)


class MeasurementsAPI(MethodView):

    # features/01-measurements/01-add-measurement.feature
    def post(self):
        
        r_details = request.get_json()
        
        try:
            timestamp = convert_to_datetime(timestamp)
        except DatetimeConversion
            
        
        return jsonify(message="Success!")

    # features/01-measurements/02-get-measurement.feature
    def get(self, timestamp):

        try:
            timestamp = convert_to_datetime(timestamp)
        except DatetimeConversionException:
            raise BadRequest(description = "Timestamp input is invalid: {}".format(timestamp))

        # TODO:
        abort(501)
