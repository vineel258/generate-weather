from data_parser.weather_parser import WeatherParser
from data_parser.location_parser import LocationParser
from utils.random_date import RandomDate
import random
import sys


if __name__ == '__main__':
    # Load Cities
    ref_cities = ['SYDNEY', 'ADELAIDE', 'MELBOURNE', 'CAIRNS', 'BRISBANE', 'CANBERRA', 'DARWIN', 'GOLDCOAST',
                  'HOBART', 'LONDON', 'NEWYORK', 'PERTH']

    # no of cities for getting weather data
    no_of_cities = 3
    if len(sys.argv) == 2:
        no_of_cities = int(sys.argv[1])
    list_of_cities = random.sample(ref_cities, no_of_cities)

    # Iterate through all the available cities and get the weather info randomly
    for city_name in list_of_cities:
        # Getting current city location details
        location = LocationParser("ref_data/location.json").get_location(city_name)
        # Get a random date within the data samples available
        date_time = RandomDate().get_random_date("2015-11-05 1:30 PM", "2016-11-05 4:50 AM")
        # Parse the weather data
        file_path = "ref_data/%s.json" % city_name
        city_info = WeatherParser(file_path)
        weather_info = city_info.get_weather_details(date_time)
        # Retrieve the weather info from weather info
        temperature = weather_info['Mean TemperatureC']
        pressure = weather_info['Mean Sea Level PressurehPa']
        conditions = weather_info['Events']
        humidity = weather_info['Mean Humidity']
        # Print the data to console with the requested format
        print "%s | %s | %s | %s | %s | %s | %s" % (city_name, location, date_time,
                                                    conditions, temperature, pressure, humidity)

