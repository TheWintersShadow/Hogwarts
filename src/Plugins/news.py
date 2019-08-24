# Created by Albus Wulfric Brain Dumbledore
# Date 2019-06-14
# Time 18:00:10

"""This script will get the local news."""

import requests

from supportClasses.NewsData import *

API_FIELDS = '?country=us&apiKey=8e8d472f7e5d470f91f513aeb7faf5f1'
NEWS_WEBSITE = 'https://newsapi.org/v2/'
TOP_NEWS = 'top-headlines'


def getTopNews():
    topNews = requests.get(NEWS_WEBSITE + TOP_NEWS + API_FIELDS)
    if topNews.status_code == 200:
        return topNews.json()
    else:
        print('Get command failed to return data.')


def getArticles(newsData):
    allArticles = dict()
    article_list = newsData['articles']
    news_number = 0
    for article in article_list:
        articleObj = NewsData()
        articleObj.Source = getSource(article)
        articleObj.Title = getTitle(article)
        articleObj.Author = getAuthor(article)
        articleObj.Description = getDescription(article)
        articleObj.ExternalURL = getURL(article)
        articleObj.ImageURL = getImageURL(article)
        articleObj.PublishedDate = getPublicationDate(article)
        articleObj.FullContent = getArticleContent(article)
        articleObj.loadData()
        allArticles[news_number] = articleObj.getAttributes()
        news_number += 1
    return allArticles


def getSource(article):
    source = article['source']['name']
    return source


def getTitle(article):
    title = article['title']
    return title


def getAuthor(article):
    author = article['author']
    return author


def getDescription(article):
    desc = article['description']
    return desc


def getURL(article):
    url = article['url']
    return url


def getImageURL(article):
    image = article['urlToImage']
    return image


def getPublicationDate(article):
    date = article['publishedAt']
    return date


def getArticleContent(article):
    content = article['content']
    return content


def main():
    topNewsData = getTopNews()
    articles = getArticles(topNewsData)
    return articles


if __name__ == '__main__':
    main()
