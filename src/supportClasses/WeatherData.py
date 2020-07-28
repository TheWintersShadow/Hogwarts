# Created by Albus Wulfric Brain Dumbledore
# Date: 7/14/2019
# Time: 11:29

import json


class WeatherData:
    def __init__(self, raw_data):
        self.raw = raw_data
        self.periods = raw_data['properties']['periods']
        self.allDays = dict()
        self.__format_periods()

    def __format_periods(self):
        day_number = 0
        for day in self.periods:
            self.allDays[day_number] = day
            day_number += 1
        return self.allDays

    def __str__(self):
        return json.dumps(self.periods, indent=3)
