# -*- coding: utf-8 -*-
import os
import requests
from scrapy import log
import scrapy
import logging
import feedparser
from stackoverflow.items import StackoverflowItem

dir = os.path.dirname(os.path.abspath(__file__))


class UserfeedSpider(scrapy.Spider):
	name = "feeds"
	allowed_domains = ['stackoverflow.com']
	start_urls = ["https://stackoverflow.com/feeds/user/USERID"]
	itertag = 'item'

	def parse_feed(self, feed):
		data = feedparser.parse(feed)

		if data.bozo:
			logging.error('Bozo feed data. %s: %r', data.bozo_exception.__class__.__name__, data.bozo_exception)
			if (hasattr(data.bozo_exception, 'getLineNumber') and hasattr(data.bozo_exception, 'getMessage')):
				line = data.bozo_exception.getLineNumber()
				logging.error('Line %d: %s', line, data.bozo_exception.getMessage())
				segment = feed.split('\n')[line-1]
				logging.info('Body segment with error: %r', segment)
			return None
		return data

	def parse(self, response):
		feed = self.parse_feed(response.body)

		if feed.entries is None:
			return False

		item = StackoverflowItem()
		for entry in feed.entries:			
			item['author'] = entry.author
			item['question'] = entry.title
			item['rank'] = entry.author
			item['link'] = entry.link
			item['publish'] = entry.published
			item['summary'] = entry.summary
			yield(item)