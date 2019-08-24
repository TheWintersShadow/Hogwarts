# Created by Albus Wulfric Brain Dumbledore
# Date 2019-06-14
# Time 18:00:02

"""This script will get the local weather."""

from requests import *

from supportClasses.WeatherData import *

WEATHER_WEBSITE = 'https://api.weather.gov/zones/zone/VAZ053/forecast'


def getWeatherData():
    weatherData = get(WEATHER_WEBSITE)
    if weatherData.status_code == 200:
        return weatherData.json()
    else:
        print('Get command failed to return data.')
        return weatherData.content


def parseData(data):
    weatherSet = WeatherData(data)
    return weatherSet.allDays


def main():
    weatherInfo = getWeatherData()
    periods = parseData(weatherInfo)
    return periods


if __name__ == '__main__':
    main()
