create_schema:
	cd collectors; python -c 'from collectors.models import job; job.create_schema(True)'

crawl_jobs:
	cd collectors; scrapy crawl indeed-job-list	

crawl_reviews:
	cd collectors; scrapy crawl indeed-comp-review

crawl_interviews:
	cd collectors; scrapy crawl glassdoor-comp-interview