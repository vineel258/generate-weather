import unittest
from data_parser.weather_parser import WeatherParser
from collections import OrderedDict


class WeatherParserTestCase(unittest.TestCase):
    """This unittest here tests around the functions created around weather parser class"""

    def test_get_weather_details_should_return_available_information(self):
        city_info = WeatherParser("../ref_data/SYDNEY.json")
        weather_info = city_info.get_weather_details("2015-11-05 1:30 PM")
        ref_data = OrderedDict([(u'Date', u'2015-11-05'), (u'Max TemperatureC', 23), (u'Mean TemperatureC', 19), (u'Min TemperatureC', 16), (u'Dew PointC', 19), (u'MeanDew PointC', 17), (u'Min DewpointC', 16), (u'Max Humidity', 100), (u'Mean Humidity', 86), (u'Min Humidity', 68), (u'Max Sea Level PressurehPa', 1019), (u'Mean Sea Level PressurehPa', 1013), (u'Min Sea Level PressurehPa', 1008), (u'Max VisibilityKm', 19), (u'Mean VisibilityKm', 8), (u'Min VisibilitykM', 4), (u'Max Wind SpeedKm', OrderedDict([(u'h', 45)])), (u'Mean Wind SpeedKm', OrderedDict([(u'h', 26)])), (u'Max Gust SpeedKm', OrderedDict([(u'h', 63)])), (u'Precipitationmm', 1.02), (u'CloudCover', 6), (u'Events', u'Rain'), (u'WindDirDegrees', 37)])
        self.assertTrue(weather_info, ref_data)

    def test_WeatherParser_should_raise_an_exception_for_invalid_city(self):
        self.assertRaises(ValueError, WeatherParser, "../ref_data/Testcity.json")

    def test_get_weather_details_should_raise_an_exception_for_invalid_attribute(self):
        city_info = WeatherParser("../ref_data/SYDNEY.json")
        self.assertRaises(ValueError, city_info.get_weather_details, '2014-11-05 1:30 PM')

if __name__ == "__main__":
    unittest.main()
