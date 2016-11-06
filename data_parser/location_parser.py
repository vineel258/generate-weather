from collections import OrderedDict
import json
import io


class LocationParser(object):
    """
    This class defines all the location related parsing
    """
    def __init__(self, file_path):
        self._data = None
        with io.open(file_path, mode='r', encoding='utf8',) as json_file:
            self._data = json.load(json_file, object_pairs_hook=OrderedDict)

    @property
    def data(self):
        """
        This function returns the parsed data info on current object
        :return: Ordered Dict
        """
        return self._data

    def get_location(self, city):
        """
        This function returns the city location from the available map
        :param city: city for which the location should be return
        :return: string, location
        """
        try:
            return '%s, %s, %s' % (self.data[city.upper()]['latitude'],
                                   self.data[city.upper()]['longitude'], self.data[city.upper()]['elevation'])
        except KeyError as known_exception:
            print known_exception
            raise ValueError('Could not find location for given city %s' % city)
