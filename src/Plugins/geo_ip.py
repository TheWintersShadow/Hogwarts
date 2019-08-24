# Created by Elijah Jeremiah Simms
# Date 2019-06-14
# Time 17:56:27

"""This is a script to turn IP addresses into Longitude and Latitude."""

from requests import *

from supportClasses.IPData import *

GEOIP_WEBSITE = 'http://ip-api.com/json/'
GEO_FIELDS = '?fields=continent,country,regionName,city,zip,lat,lon,timezone,isp,reverse,mobile,query'
IP_Data = IPData()


def getIP(IP_addr):
    ipData = get(GEOIP_WEBSITE + IP_addr + GEO_FIELDS)
    if ipData.status_code == 200:
        return ipData.json()
    else:
        print('Get command failed to return data.')


def getIPAddr(data):
    IP_Data.IP = data['query']


def getContinent(data):
    IP_Data.continent = data['continent']


def getCountry(data):
    IP_Data.country = data['country']


def getRegionName(data):
    IP_Data.regionName = data['regionName']


def getCity(data):
    IP_Data.city = data['city']


def getZip(data):
    IP_Data.zip = data['zip']


def getLat(data):
    IP_Data.latitude = data['lat']


def getLon(data):
    IP_Data.longitude = data['lon']


def getTimeZone(data):
    IP_Data.timeZone = data['timezone']


def getISP(data):
    IP_Data.isp = data['isp']


def getDNS(data):
    IP_Data.reverse = data['reverse']


def getMobile(data):
    IP_Data.mobile = data['mobile']


def main(IP_addr):
    locationData = getIP(IP_addr)
    getIPAddr(locationData)
    getContinent(locationData)
    getCountry(locationData)
    getRegionName(locationData)
    getCity(locationData)
    getZip(locationData)
    getLat(locationData)
    getLon(locationData)
    getTimeZone(locationData)
    getISP(locationData)
    getDNS(locationData)
    getMobile(locationData)
    IP_Data.loadData()
    return IP_Data.getAttributes()


if __name__ == '__main__':
    main(IP_addr)
