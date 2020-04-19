# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from models.job import JobPost, create_session, close_session, CompanyReview, JobInterview
from datetime import datetime

PIPELINE_SPIDERS = {
    'IndeedJobListCollectorPipeline': ['indeed-job-list'],
    'IndeedCompReviewCollectorPipeline': ['indeed-company-review'],
    'GlassdoorJobListCollectorPipeline': ['glassdoor-job-list'],
    'GlassdoorInterviewCollectorPipeline': ['glassdoor-job-interview'],
} 

class IndeedJobListCollectorPipeline(object):
    def __init__(self):
        self.session = create_session()

    def open_spider(self, spider):
        print('Start spider...'+spider.name)

    def close_spider(self, spider):
        print('Stop spider... '+spider.name)
        close_session(self.session)

    def process_item(self, item, spider):
        spider_name = spider.name
        if spider_name not in PIPELINE_SPIDERS[self.__class__.__name__]:
            return item

        jobPost = JobPost(title=item['title'], \
            company=item['company'], \
            location=item['location'], \
            description=item['description'], \
            source=item['source'], \
            search_kw=item['search_kw'])
        
        self.session.add(jobPost)
        self.session.commit()
        return item


class IndeedCompReviewCollectorPipeline(object):
    def __init__(self):
        self.session = create_session()

    def open_spider(self, spider):
        print('Start spider...'+spider.name)

    def close_spider(self, spider):
        print('Stop spider... '+spider.name)
        close_session(self.session)

    def process_item(self, item, spider):
        spider_name = spider.name
        if spider_name not in PIPELINE_SPIDERS[self.__class__.__name__]:
            return item

        compReview = CompanyReview(company = item['company'], \
                title = item['title'], \
                rating = item['rating'], \
	            author = item['author'], \
	            author_status = item['author_status'], \
                location = item['location'], \
                date = item['date'], \
                description = item['description'], \
                source = item['source'])
        
        self.session.add(compReview)
        self.session.commit()
        return item

class GlassdoorJobListCollectorPipeline(object):
    def __init__(self):
        self.session = create_session()

    def open_spider(self, spider):
        print('Start spider...'+spider.name)

    def close_spider(self, spider):
        print('Stop spider... '+spider.name)
        close_session(self.session)

    def process_item(self, item, spider):
        spider_name = spider.name
        if spider_name not in PIPELINE_SPIDERS[self.__class__.__name__]:
            return item

        jobPost_glassdoor = JobPost(title=item['title'], \
            company=item['company'], \
            location=item['location'], \
            description=item['description'], \
            source=item['source'], \
            search_kw=item['search_kw'])
        
        self.session.add(jobPost_glassdoor)
        self.session.commit()
        return item

class GlassdoorInterviewCollectorPipeline(object):
    def __init__(self):
        self.session = create_session()

    def open_spider(self, spider):
        print('Start spider...'+spider.name)

    def close_spider(self, spider):
        print('Stop spider... '+spider.name)
        close_session(self.session)

    def process_item(self, item, spider):
        spider_name = spider.name
        if spider_name not in PIPELINE_SPIDERS[self.__class__.__name__]:
            return item

        jobInterview = JobInterview(company = item['company'], \
                title = item['title'], \
                question = item['question'], \
                date = item['date'], \
                source = item['source'], \
                search_kw=item['search_kw'])
        
        self.session.add(jobInterview)
        self.session.commit()
        return item
