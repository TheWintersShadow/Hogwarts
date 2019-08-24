# Created by Albus Wulfric Brain Dumbledore
# Date 2019-06-15
# Time 09:13:46

"""This is the class structure for each news article."""

import json


class NewsData:
    def __init__(self):
        self.Source = None
        self.Title = None
        self.Author = None
        self.Description = None
        self.ExternalURL = None
        self.ImageURL = None
        self.PublishedDate = None
        self.FullContent = None
        self.attributes = {}

    def __str__(self):
        return json.dumps(self.attributes, indent=3)

    def loadData(self):
        self.attributes['Source'] = self.Source
        self.attributes['Title'] = self.Title
        self.attributes['Author'] = self.Author
        self.attributes['Description'] = self.Description
        self.attributes['External URL'] = self.ExternalURL
        self.attributes['Image URL'] = self.ImageURL
        self.attributes['Publication Date'] = self.PublishedDate
        self.attributes['Article Content'] = self.FullContent

    def getAttributes(self):
        return self.attributes
