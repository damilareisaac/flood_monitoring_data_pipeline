from marshmallow import Schema, fields
from marshmallow.decorators import pre_dump
import pandas as pd


class StationSchema(Schema):
    eaAreaName = fields.String(dump_default=None)
    easting = fields.String(dump_default=None)
    gridReference = fields.String(dump_default=None)
    label = fields.String(dump_default=None)
    lat = fields.String(dump_default=None)
    long = fields.String(dump_default=None)
    measures_label = fields.String(dump_default=None)
    measures_latestReading_value = fields.String(
        data_key="measure_value", dump_default=None
    )
    measures_latestReading_dateTime = fields.String(
        data_key="measure_date_time", dump_default=None
    )
    measures_latestReading_date = fields.String(
        data_key="measure_date", dump_default=None
    )
    measures_notation = fields.String(dump_default=None)
    measures_parameter = fields.String(dump_default=None)
    measures_parameterName = fields.String(dump_default=None)
    measures_period = fields.String(dump_default=None)
    measures_qualifier = fields.String(dump_default=None)
    measures_valueType = fields.String(dump_default=None)
    stationReference = fields.String(dump_default=None)
    northing = fields.String(dump_default=None)

    @pre_dump
    def flatten_nested_station_data(self, data, *args, **kwargs) -> dict:
        try:
            data = pd.json_normalize(data, sep="_")
            return data.to_dict(orient="records")[0]
        except Exception:
            return {}
