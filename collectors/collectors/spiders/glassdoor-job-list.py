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
from ..items import GlassdoorJobItem

MAX_JOBS = 20

class GlassdoorJobListSpider(scrapy.Spider):
    name = 'glassdoor-job-list'
    allowed_domains = ['glassdoor.com']
    start_urls = ['https://www.glassdoor.ca/Job']
    

    def __init__(self):
        self.jobs_scraped = 0
        self.session = create_session()

    def start_requests(self):
        urls = self.start_urls
        q = "vancouver-data-scientist-jobs-SRCH_IL.0,9_IC2278756_KO10,24.htm"
        for url in urls:
            yield scrapy.Request(url="{0}/{1}".format(url,q), callback=self.parse)

    def parse(self, response):
        url = response.url
        # start the webdriver to crawl reviews
        chrome_options = Options()  
        driver = webdriver.Chrome(chrome_options=chrome_options)
        try:
            #driver.get('chrome://settings/')
            #driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.70);')
            driver.get(url)
            
            job_containers = driver.find_elements_by_css_selector('.jlGrid.hover')
            for job_element in job_containers:
                self.jobs_scraped += 1
                if (self.jobs_scraped > MAX_JOBS):
                    return

                
                job_title = job_element.find_element_by_css_selector('.jobLink.jobInfoItem.jobTitle').text    
                job_company = job_element.find_element_by_css_selector('.jobInfoItem.jobEmployerName').text
                
                

                job_link = job_element.find_element_by_css_selector('li.jl')
                job_link.click()
                time.sleep(2)
                job_location = job_element.find_element_by_css_selector('.location').text
                job_description = driver.find_element_by_css_selector('.jobDescriptionContent.desc').text

                job_item = GlassdoorJobItem()
                job_item['title'] = job_title
                job_item['company'] = job_company
                job_item['location'] = job_location
                job_item['description'] = job_description
                job_item['source'] = 'glassdoor.com'
                
                yield job_item
            
            # move to the next page of job list
            #next_page = driver.find_elements_by_css_selector('.pagingControls.cell.middle li')[-1]
            next_page = driver.find_elements_by_css_selector('li.page a')[-1]
            print('NEXT PAGE: %s' %next_page)
            if next_page:
                yield scrapy.Request(next_page.get_attribute('href'), callback=self.parse)
                            
        except Exception as e:
            print(e)

        driver.close()