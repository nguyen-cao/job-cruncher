create_schema:
	cd collectors; python -c 'from collectors.models import job; job.create_schema(True)'

crawl_jobs:
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+scientist&l=Vancouver%2C+BC' -a max_items=25 -a search_kw='data scientist'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+engineer&l=Vancouver%2C+BC' -a max_items=5 -a search_kw='data engineer'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+scientist&l=Toronto%2C+ON' -a max_items=5 -a search_kw='data scientist'

crawl_reviews:
	cd collectors; scrapy crawl indeed-company-review -a query='Air-Canada/reviews?fcountry=CA&lang=en' -a max_items=5

crawl_jobs_glassdoor:
	cd collectors; scrapy crawl glassdoor-job-list -a query='vancouver-data-scientist-jobs-SRCH_IL.0,9_IC2278756_KO10,24.htm' -a max_items=5 -a search_kw='data scientist'
	cd collectors; scrapy crawl glassdoor-job-list -a query='toronto-data-engineer-jobs-SRCH_IL.0,7_IC2281069_KO8,21.htm' -a max_items=5 -a search_kw='data engineer'

crawl_interviews:
	cd collectors; scrapy crawl glassdoor-job-interview -a query='data-scientist-interview-questions-SRCH_KO0,14.htm' -a max_items=5 -a search_kw='data scientist'

pull_images:
	docker pull jupyter/scipy-notebook

run_jupyter:
	docker run --rm --name job-cruncher -e JUPYTER_ENABLE_LAB=yes -w /home/jovyan/work -u root -v ${PWD}:/home/jovyan/work -p 8888:8888 jupyter/scipy-notebook