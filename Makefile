create_schema:
	cd collectors; python -c 'from collectors.models import job; job.create_schema(True)'

crawl_jobs:
	cd collectors; scrapy crawl indeed-job-list

crawl_jobs_glassdoor:
	cd collectors; scrapy crawl glassdoor-job-list