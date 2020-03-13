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
from ..items import GlassdoorInterviewItem

MAX_INTERVIEWS = 25

class GlassdoorInterviewSpider(scrapy.Spider):
    name = 'glassdoor-job-interview'
    allowed_domains = ['glassdoor.ca']
    start_urls = ['https://www.glassdoor.ca/Interview/']

    def __init__(self):
        self.interviews_scraped = 0
        self.session = create_session()
        self.num_pages = 1

    def start_requests(self):
        urls = self.start_urls
        q = "data-scientist-interview-questions-SRCH_KO0,14.htm"
        for url in urls:
            yield scrapy.Request(url="{0}/{1}".format(url,q), callback=self.parse)

    def parse(self, response):
        print("Inside PArse............!!!!!!")
        url = response.url
        print("url=====",url)
        # start the webdriver to crawl reviews
        chrome_options = Options()  
        driver = webdriver.Chrome(chrome_options=chrome_options)
        try:
            driver.get(url)
            
            interview_containers = driver.find_elements_by_css_selector('.interviewQuestion.noPad')
            for interview_element in interview_containers:
                self.interviews_scraped += 1
                if (self.interviews_scraped > MAX_INTERVIEWS):
                    return

                author_info = interview_element.find_element_by_css_selector('.authorInfo').text.split(' at ')
                interview_company = author_info[1].replace('was asked...','')
                interview_title = author_info[0]
                interview_date = interview_element.find_element_by_css_selector('.cell.alignRt.noWrap.minor.hideHH').text
                interview_question = interview_element.find_element_by_css_selector('.questionText').text             
                time.sleep(2)
    
                interview_item = GlassdoorInterviewItem()
                interview_item['company'] = interview_company
                interview_item['title'] = interview_title
                interview_item['question'] = interview_question
                interview_item['date'] = interview_date
                interview_item['source'] = 'glassdoor.com'
                
                yield interview_item
            
            # move to the next page of interview list
            next_page = driver.find_elements_by_css_selector('.next a')[0]
            # print("SSsssssssssssssssssssss",next_page)
            # print("*******************************************")
            print('NEXT PAGE: %s' %next_page)
            if next_page:
            #     # yield scrapy.Request(next_page.get_attribute('href'), callback=self.parse)
            #     print("YIELD= ",scrapy.Request(next_page.get_attribute('href'), callback=self.parse))
                yield scrapy.Request(next_page.get_attribute('href'), callback=self.parse)

            # self.num_pages += 1
            # temp = 'https://www.glassdoor.ca/Interview/'
            # q = "data-scientist-interview-questions-SRCH_KO0,14"
            # print("*******************************************")
            # print(temp+q+"_IP"+str(self.num_pages)+".htm")
            # yield scrapy.Request(temp+q+"_IP"+str(self.num_pages)+".htm", callback=self.parse)

                            
        except Exception as e:
            print(e)

        driver.close()