# Created by Albus Wulfric Brain Dumbledore
# Date 2019-06-14
# Time 18:00:10

"""This script will get the local news."""

import requests, xmltodict
from supportClasses.NewsData import *

API_FIELDS = '?country=us&apiKey=8e8d472f7e5d470f91f513aeb7faf5f1'
NEWS_WEBSITE = 'https://newsapi.org/v2/'
TOP_NEWS = 'top-headlines'

NYT_URL = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"


def getTechNews():
    topNews = requests.get(NEWS_WEBSITE + TOP_NEWS + API_FIELDS)
    tech_news = requests.get(NYT_URL)
    if tech_news.status_code == 200:
        return xmltodict.parse(tech_news.content)
    else:
        print('Get command failed to return data.')


def getArticles(newsData):
    allArticles = dict()
    article_list = newsData['rss']['channel']['item']
    news_number = 0
    for article in article_list:
        articleObj = NewsData()
        articleObj.Source = getSource(article)
        articleObj.Title = getTitle(article)
        articleObj.Author = getAuthor(article)
        articleObj.Description = getDescription(article)
        articleObj.ExternalURL = getURL(article)
        #articleObj.ImageURL = getImageURL(article)
        articleObj.PublishedDate = getPublicationDate(article)
        articleObj.loadData()
        allArticles[news_number] = articleObj.getAttributes()
        news_number += 1
    return allArticles


def getSource(article):
    source = 'New York Times'
    return source


def getTitle(article):
    title = article['title']
    return title


def getAuthor(article):
    author = article['dc:creator']
    return author


def getDescription(article):
    desc = article['description']
    return desc


def getURL(article):
    url = article['link']
    return url


def getImageURL(article):
    image = article['media:content']['@url']
    return image


def getPublicationDate(article):
    date = article['pubDate'][:-15]
    return date


def main():
    topNewsData = getTechNews()
    articles = getArticles(topNewsData)
    return articles


if __name__ == '__main__':
    main()
