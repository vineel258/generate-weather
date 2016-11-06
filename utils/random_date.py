import random
import time


class RandomDate(object):
    """
    This class generates the random dates within specified range
    """

    def str_time_prop(self, start, end, date_format):
        """Get a time at a proportion of a range of two formatted times.

        start and end should be strings specifying times formated in the
        given format (strftime-style), giving an interval [start, end].
        prop specifies how a proportion of the interval to be taken after
        start.  The returned time will be in the specified format.
        :param start: Start date range
        :param end: End date range
        :param date_format: date format required
        """

        stime = time.mktime(time.strptime(start, date_format))
        etime = time.mktime(time.strptime(end, date_format))

        ptime = stime + random.random() * (etime - stime)

        return time.strftime(date_format, time.localtime(ptime))

    def get_random_date(self, start, end):
        return self.str_time_prop(start, end, '%Y-%m-%d %I:%M %p')
