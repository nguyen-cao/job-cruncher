create_schema:
	cd collectors; python -c 'from collectors.models import job; job.create_schema(True)'

crawl_jobs:
	cd collectors; scrapy crawl indeed-job-list	

crawl_reviews:
	cd collectors; scrapy crawl indeed-company-review

crawl_jobs_glassdoor:
	cd collectors; scrapy crawl glassdoor-job-list

crawl_interviews:
	cd collectors; scrapy crawl glassdoor-job-interview

pull_images:
	docker pull jupyter/scipy-notebook

run_jupyter:
	docker run --rm --name job-cruncher -e JUPYTER_ENABLE_LAB=yes -w /home/jovyan/work -u root -v ${PWD}:/home/jovyan/work -p 8888:8888 jupyter/scipy-notebook