# Created by Albus Wulfric Brain Dumbledore
# Date 2019-06-14
# Time 18:00:21

"""This script gets the quote of the day."""

from requests import *

QUOTE_WEBSITE = 'http://quotes.rest/qod'


def getQuoteData():
    quoteData = get(QUOTE_WEBSITE)
    if quoteData.status_code == 200:
        return quoteData.json()
    else:
        print('Get command failed to return data.')


def getQuote(qData):
    quote = qData['contents']['quotes'][0]['quote']
    return quote


def getAuthor(qData):
    author = qData['contents']['quotes'][0]['author']
    return author


def main():
    quoteInfo = getQuoteData()
    quote = getQuote(quoteInfo)
    author = getAuthor(quoteInfo)
    return quote, author


if __name__ == '__main__':
    main()
