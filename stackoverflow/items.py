# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StackoverflowItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    question = scrapy.Field()
    rank = scrapy.Field()
    link = scrapy.Field()
    publish = scrapy.Field()
    summary = scrapy.Field()
