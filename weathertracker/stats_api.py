from flask import request, jsonify
from flask.views import MethodView
from werkzeug.exceptions import abort, BadRequest
from weathertracker.stats import get_stats
from weathertracker.utils.conversion import (
    convert_to_datetime,
    DatetimeConversionException,
)


class StatsAPI(MethodView):
    # features/02-stats/01-get-stats.feature
    def get(self):
        stats = request.args.getlist("stat")
        if len(stats) == 0:
            raise BadRequest("No stats were provided.")
        metrics = request.args.getlist("metric")
        if len(metrics) == 0:
            raise BadRequest("No metrics were provided.")
        from_datetime = request.args.get("fromDateTime")
        if from_datetime is None:
            raise BadRequest("fromDateTime was not provided.")
        to_datetime = request.args.get("toDateTime")
        if to_datetime is None:
            raise BadRequest("toDateTime was not provided.")
            
        try:
            from_datetime = convert_to_datetime(from_datetime)
            to_datetime = convert_to_datetime(to_datetime)
        except DatetimeConversionException:
            raise BadRequest(description = "Timestamp input is invalid.")

        stats = get_stats(stats, metrics, from_datetime, to_datetime)
        return jsonify(stats)
