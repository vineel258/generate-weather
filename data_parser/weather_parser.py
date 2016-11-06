from collections import OrderedDict
from collections import Iterable
import json
import io


class WeatherParser(object):
    def __init__(self, file_path):
        self._data = None
        try:
            with io.open(file_path, mode='r', encoding='utf8',) as json_file:
                self._data = json.load(json_file, object_pairs_hook=OrderedDict)
        except IOError as known_exception:
            print known_exception
            raise ValueError('Please try with a valid city')

    @property
    def data(self):
        return self._data

    def get_weather_details(self, date):
        """
        This function returns the weather information for current city on given date
        :param date: date requested for weather
        :return: weather information
        """
        if not isinstance(self.data, Iterable):
            raise TypeError('Weather data not found, please try with a valid data')
        for temp_date in self.data:
            if temp_date['Date'] in date:
                return temp_date
        raise ValueError('Could not find information on date %s' % date)
