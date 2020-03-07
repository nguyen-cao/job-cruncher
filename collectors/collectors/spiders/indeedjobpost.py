# -*- coding: utf-8 -*-
import scrapy


class IndeedjobpostSpider(scrapy.Spider):
    name = 'indeedjobpost'
    allowed_domains = ['https://ca.indeed.com']
    start_urls = ['http://https://ca.indeed.com/']

    def parse(self, response):
        pass
