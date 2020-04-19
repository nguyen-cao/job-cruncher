# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from .indeed_job_list import IndeedJobListSpider
from .glassdoor_job_list import GlassdoorJobListSpider
from .indeed_comp_reviews import IndeedCompReviewSpider
from .glassdoor_interviews import GlassdoorInterviewSpider

CRAWLERS = {
    'indeed-job-list': IndeedJobListSpider,
    'glassdoor-job-list': GlassdoorJobListSpider,
    'indeed-company-review': IndeedCompReviewSpider,
    'glassdoor-job-interview': GlassdoorInterviewSpider
}