# Created by Albus Wulfric Brain Dumbledore
# Date 2019-06-14
# Time 19:15:40

"""This is the class structure for IP Location data."""

import json


class IPData:
    def __init__(self):
        self.continent = None
        self.country = None
        self.regionName = None
        self.city = None
        self.zip = None
        self.timeZone = None
        self.latitude = None
        self.longitude = None
        self.isp = None
        self.reverse = None
        self.mobile = bool
        self.IP = None
        self.attributes = {}

    def __str__(self):
        return json.dumps(self.attributes, indent=3)

    def loadData(self):
        self.attributes['IP'] = self.IP
        self.attributes['Continent'] = self.continent
        self.attributes['Country'] = self.country
        self.attributes['Region Name'] = self.regionName
        self.attributes['City'] = self.city
        self.attributes['Zip'] = self.zip
        self.attributes['Time Zone'] = self.timeZone
        self.attributes['Latitude'] = self.latitude
        self.attributes['Longitude'] = self.longitude
        self.attributes['ISP'] = self.isp
        self.attributes['Reverse DNS Lookup'] = self.reverse
        self.attributes['Is a mobile device'] = self.mobile

    def getAttributes(self):
        return self.attributes
