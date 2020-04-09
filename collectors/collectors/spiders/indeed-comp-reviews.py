# -*- coding: utf-8 -*-
import scrapy
import time
import os
import re
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from ..models.job import create_session
from ..items import IndeedReviewItem

class IndeedCompReviewSpider(scrapy.Spider):
    name = 'indeed-company-review'
    allowed_domains = ['indeed.com']
    start_urls = ['https://ca.indeed.com/cmp']

    def __init__(self, query=None, max_items=1, search_kw=None, *args, **kwargs):
        super(IndeedCompReviewSpider, self).__init__(*args, **kwargs)
        self.query = query
        self.search_kw = search_kw if search_kw != None else ''
        self.max_items = int(max_items)
        self.reviews_scraped = 0
        self.session = create_session()

    def start_requests(self):
        urls = self.start_urls
        if self.query != None:
            for url in urls:
                yield scrapy.Request(url="{0}/{1}".format(url,self.query), callback=self.parse)

    def parse(self, response):
        url = response.url
        # start the webdriver to crawl reviews
        chrome_options = Options()  
        driver = webdriver.Chrome(chrome_options=chrome_options)
        try:
            driver.get(url)
            
            review_containers = driver.find_elements_by_css_selector('.cmp-ReviewsList-container')
            
            for review_element in review_containers:
                self.reviews_scraped += 1
                if (self.reviews_scraped > self.max_items):
                    return

                review_company = self.search_kw # To be generalized
                review_title = review_element.find_element_by_css_selector('.cmp-Review-title').text
                review_rating = review_element.find_element_by_css_selector('.cmp-ReviewRating-text').text
                review_author = review_element.find_element_by_css_selector('.cmp-ReviewAuthor-link').text
                details = review_element.find_element_by_css_selector('.cmp-ReviewAuthor').text
                # Manipulating the data to get relevant information
                review_author, details = details.split("(")
                review_author_status, details = details.split(")")
                review_location, review_date = details.split("-", 2)[1:]
                review_author_status = review_author_status.replace(")", "")
                review_description = review_element.find_element_by_css_selector('.cmp-Review-text').text
                time.sleep(2)
    
                review_item = IndeedReviewItem()
                review_item['company'] = review_company
                review_item['title'] = review_title
                review_item['rating'] = review_rating
                review_item['author'] = review_author
                review_item['author_status'] = review_author_status
                review_item['location'] = review_location
                review_item['date'] = review_date
                review_item['description'] = review_description
                review_item['source'] = 'indeed.com'
                
                yield review_item
            
            # move to the next page of job list
            next_page = driver.find_elements_by_css_selector('.cmp-Pagination a')[-1]
            print('NEXT PAGE: %s' %next_page)
            if next_page:
                yield scrapy.Request(next_page.get_attribute('href'), callback=self.parse)
                            
        except Exception as e:
            print(e)

        driver.close()