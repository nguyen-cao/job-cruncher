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
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options

from ..models.job import create_session
from ..items import GlassdoorJobItem, IndeedJobItem

class GlassdoorJobListSpider(scrapy.Spider):
    name = 'glassdoor-job-list'
    allowed_domains = ['glassdoor.ca']
    start_urls = ['https://www.glassdoor.ca/Job']
    

    def __init__(self, query=None, max_items=1, search_kw=None, *args, **kwargs):
        super(GlassdoorJobListSpider, self).__init__(*args, **kwargs)
        self.query = query
        self.search_kw = search_kw if search_kw != None else ''
        self.max_items = int(max_items)
        self.jobs_scraped = 0
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
            
            job_containers = driver.find_elements_by_css_selector('.jobContainer')
            for job_element in job_containers:
                self.jobs_scraped += 1
                if (self.jobs_scraped > self.max_items):
                    return

                try:
                    driver.find_element_by_class_name("selected").click()
                except ElementClickInterceptedException:
                    pass

                time.sleep(.1)

                # Trying to bypass Glassdoor login
                try:
                    driver.find_element_by_css_selector(".SVGInline.modal_closeIcon").click()  #clicking to the X.
                except NoSuchElementException:
                    pass

                job_title = job_element.find_elements_by_css_selector('.jobInfoItem.jobTitle')[1].text    
                job_company = job_element.find_element_by_css_selector('.jobInfoItem.jobEmpolyerName').text
                job_location = job_element.find_element_by_css_selector('.loc').text

                job_link = job_element.find_element_by_css_selector('.jobLink.jobInfoItem.jobTitle')
                job_link.click()
                time.sleep(2)
                
                job_description = driver.find_element_by_css_selector('.jobDescriptionContent.desc').text

                job_item = GlassdoorJobItem()
                # job_item = IndeedJobItem()
                job_item['title'] = job_title
                job_item['company'] = job_company
                job_item['location'] = job_location
                job_item['description'] = job_description
                job_item['source'] = 'glassdoor.com'
                job_item['search_kw'] = self.search_kw
                
                yield job_item
            
            # move to the next page of job list
            #next_page = driver.find_elements_by_css_selector('.pagingControls.cell.middle li')[-1]
            # next_page = driver.find_element_by_css_selector('.next a')
            next_page = driver.find_elements_by_css_selector('.next a')[0]
            print('NEXT PAGE: %s' %next_page)
            if next_page:
                yield scrapy.Request(next_page.get_attribute('href'), callback=self.parse)
                            
        except Exception as e:
            print(e)

        driver.close()