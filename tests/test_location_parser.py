import unittest
from data_parser.location_parser import LocationParser


class WeatherParserTestCase(unittest.TestCase):
    """This unittest here tests around the functions created around weather parser class"""

    def test_get_location_should_return_available_location_details(self):
        city_info = LocationParser("../ref_data/location.json")
        self.assertEqual("-33.8688197, 151.2092955, 25", city_info.get_location('SYDNEY'))

    def test_get_location_should_return_available_local_details_ignore_case(self):
        city_info = LocationParser("../ref_data/location.json")
        self.assertEqual("-33.8688197, 151.2092955, 25", city_info.get_location('sydney'))
        self.assertEqual("-33.8688197, 151.2092955, 25", city_info.get_location('SyDNEY'))

    def test_get_weather_details_should_raise_an_exception_for_invalid_attribute(self):
        city_info = LocationParser("../ref_data/location.json")
        self.assertRaises(ValueError, city_info.get_location, 'Invalid')

if __name__ == "__main__":
    unittest.main()
