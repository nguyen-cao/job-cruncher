# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CollectorsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class IndeedJobItem(scrapy.Item):
    
	# the fields for the item are defined here like:
	# job
	title = scrapy.Field()
	company = scrapy.Field()
	location = scrapy.Field()
	description = scrapy.Field()
	source = scrapy.Field()


class IndeedReviewItem(scrapy.Item):
    
	# the fields for the item are defined here like:
	# review
	title = scrapy.Field()
	rating = scrapy.Field()
	author = scrapy.Field()
	status = scrapy.Field()
	location = scrapy.Field()
	date = scrapy.Field()
	description = scrapy.Field()
	helpful_yes = scrapy.Field()
	helpful_no = scrapy.Field()
	source = scrapy.Field()