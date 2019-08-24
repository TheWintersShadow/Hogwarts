# Created by Albus Wulfric Brain Dumbledore
# Date 2019-06-14
# Time 18:00:35

import json

import Plugins.geo_ip as geo
import Plugins.news as news
import Plugins.quote as quote
import Plugins.weather as weather


def main():
    # ToDo Maybe create one big JSON with all the data and pass that to parse?
    IP_Geo = geo.main('174.204.9.115')
    print(json.dumps(IP_Geo, indent=3))
    QoD = dict()
    QoD['Quote'], QoD['Author'] = quote.main()
    print(QoD)
    newsArticles = news.main()
    for article in newsArticles:
        print(json.dumps(article, indent=3))
    weatherData = weather.main()
    for period in weatherData:
        print(json.dumps(period, indent=3))


if __name__ == '__main__':
    main()
