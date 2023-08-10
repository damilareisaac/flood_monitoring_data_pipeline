from station_schema import StationSchema
import unittest
from unittest import TestCase


class SchemaTestCase(TestCase):
    def setUp(self):
        self.station_schema = StationSchema()
        self.test_data = {
            "@id": "http://environment.data.gov.uk/flood-monitoring/id/stations/SJ37_030",
            "eaRegionName": "North West",
            "gridReference": "SJ3073",
            "label": "Burton Point Deep",
            "measures": {
                "@id": "http://environment.data.gov.uk/flood-monitoring/id/measures/SJ37_030-level-groundwater-i-1_h-m",
                "label": "Burton Point Deep - level-groundwater-i-1_h-m",
                "latestReading": {
                    "@id": "http://environment.data.gov.uk/flood-monitoring/data/readings/SJ37_030-level-groundwater-i-1_h-m/2022-06-07T02-00-00Z",
                    "date": "2022-06-07",
                    "dateTime": "2022-06-07T02:00:00Z",
                    "measure": "http://environment.data.gov.uk/flood-monitoring/id/measures/SJ37_030-level-groundwater-i-1_h-m",
                    "value": 0.479,
                },
                "notation": "SJ37_030-level-groundwater-i-1_h-m",
                "parameter": "level",
                "parameterName": "Water Level",
                "period": 3600,
                "qualifier": "Groundwater",
                "station": "http://environment.data.gov.uk/flood-monitoring/id/stations/SJ37_030",
                "stationReference": "SJ37_030",
                "type": [
                    "http://environment.data.gov.uk/flood-monitoring/def/core/Measure",
                    "http://environment.data.gov.uk/flood-monitoring/def/core/WaterLevel",
                ],
                "unit": "http://qudt.org/1.1/vocab/unit#Meter",
                "unitName": "m",
                "valueType": "instantaneous",
            },
            "notation": "SJ37_030",
            "stationReference": "SJ37_030",
            "type": "http://environment.data.gov.uk/flood-monitoring/def/core/Station",
        }

        self.expected_result = {
            "gridReference": "SJ3073",
            "label": "Burton Point Deep",
            "measures_label": "Burton Point Deep - level-groundwater-i-1_h-m",
            "measure_value": 0.479,
            "measure_date_time": "2022-06-07T02:00:00Z",
            "measure_date": "2022-06-07",
            "measures_notation": "SJ37_030-level-groundwater-i-1_h-m",
            "measures_parameter": "level",
            "measures_parameterName": "Water Level",
            "measures_period": "3600",
            "measures_qualifier": "Groundwater",
            "measures_valueType": "instantaneous",
            "stationReference": "SJ37_030",
        }

    def test_dump(self):
        print("This called")
        result = self.station_schema.dump(self.test_data)
        self.assertEquals(result, self.expected_result)


if __name__ == "__main__":
    unittest.main()
