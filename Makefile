create_schema:
	cd collectors; python -c 'from collectors.models import job; job.create_schema(True)'

crawl_jobs:
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+scientist&l=Vancouver%2C+BC' -a max_items=5 -a search_kw='data scientist'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+engineer&l=Vancouver%2C+BC' -a max_items=5 -a search_kw='data engineer'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+analyst&l=Vancouver%2C+BC' -a max_items=5 -a search_kw='data analyst'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+scientist&l=Toronto%2C+ON' -a max_items=5 -a search_kw='data scientist'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+engineer&l=Toronto%2C+ON' -a max_items=5 -a search_kw='data engineer'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+analyst&l=Toronto%2C+ON' -a max_items=5 -a search_kw='data analyst'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+scientist&l=Montreal%2C+QC' -a max_items=5 -a search_kw='data scientist'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+engineer&l=Montreal%2C+QC' -a max_items=5 -a search_kw='data engineer'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+analyst&l=Montreal%2C+QC' -a max_items=5 -a search_kw='data analyst'

crawl_jobs_production:
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+scientist&l=Vancouver%2C+BC' -a max_items=1000 -a search_kw='data scientist'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+engineer&l=Vancouver%2C+BC' -a max_items=1000 -a search_kw='data engineer'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+analyst&l=Vancouver%2C+BC' -a max_items=1000 -a search_kw='data analyst'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+scientist&l=Toronto%2C+ON' -a max_items=1000 -a search_kw='data scientist'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+engineer&l=Toronto%2C+ON' -a max_items=1000 -a search_kw='data engineer'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+analyst&l=Toronto%2C+ON' -a max_items=1000 -a search_kw='data analyst'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+scientist&l=Montreal%2C+QC' -a max_items=1000 -a search_kw='data scientist'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+engineer&l=Montreal%2C+QC' -a max_items=1000 -a search_kw='data engineer'
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+analyst&l=Montreal%2C+QC' -a max_items=1000 -a search_kw='data analyst'

crawl_jobs_posts:
	cd collectors; scrapy crawl indeed-job-list	-a query='q=data+scientist&l=Vancouver%2C+BC' -a max_items=3 -a search_kw='data scientist'
	cd collectors; scrapy crawl glassdoor-job-list -a query='toronto-data-engineer-jobs-SRCH_IL.0,7_IC2281069_KO8,21.htm' -a max_items=3 -a search_kw='data engineer'

crawl_reviews:
	cd collectors; scrapy crawl indeed-company-review -a query='Air-Canada/reviews?fcountry=CA&lang=en' -a max_items=5

crawl_jobs_glassdoor:
	cd collectors; scrapy crawl glassdoor-job-list -a query='vancouver-data-scientist-jobs-SRCH_IL.0,9_IC2278756_KO10,24.htm' -a max_items=5 -a search_kw='data scientist'
	cd collectors; scrapy crawl glassdoor-job-list -a query='toronto-data-engineer-jobs-SRCH_IL.0,7_IC2281069_KO8,21.htm' -a max_items=5 -a search_kw='data engineer'

crawl_jobs_glassdoor_production:
	cd collectors; scrapy crawl glassdoor-job-list -a query='vancouver-data-scientist-jobs-SRCH_IL.0,9_IC2278756_KO10,24.htm' -a max_items=1000 -a search_kw='data scientist'
	cd collectors; scrapy crawl glassdoor-job-list -a query='vancouver-data-engineer-jobs-SRCH_IL.0,9_IC2278756_KO10,23.htm' -a max_items=1000 -a search_kw='data engineer'
	cd collectors; scrapy crawl glassdoor-job-list -a query='vancouver-data-analyst-jobs-SRCH_IL.0,9_IC2278756_KO10,22.htm' -a max_items=1000 -a search_kw='data analyst'
	cd collectors; scrapy crawl glassdoor-job-list -a query='toronto-data-scientist-jobs-SRCH_IL.0,7_IC2281069_KO8,22.htm' -a max_items=1000 -a search_kw='data scientist'
	cd collectors; scrapy crawl glassdoor-job-list -a query='toronto-data-engineer-jobs-SRCH_IL.0,7_IC2281069_KO8,21.htm' -a max_items=1000 -a search_kw='data engineer'
	cd collectors; scrapy crawl glassdoor-job-list -a query='toronto-data-analyst-jobs-SRCH_IL.0,7_IC2281069_KO8,20.htm' -a max_items=1000 -a search_kw='data analyst'
	cd collectors; scrapy crawl glassdoor-job-list -a query='montreal-data-scientist-jobs-SRCH_IL.0,8_IC2296722_KO9,23.htm' -a max_items=1000 -a search_kw='data scientist'
	cd collectors; scrapy crawl glassdoor-job-list -a query='montreal-data-engineer-jobs-SRCH_IL.0,8_IC2296722_KO9,22.htm' -a max_items=1000 -a search_kw='data engineer'
	cd collectors; scrapy crawl glassdoor-job-list -a query='montreal-data-analyst-jobs-SRCH_IL.0,8_IC2296722_KO9,21.htm' -a max_items=1000 -a search_kw='data analyst'

crawl_interviews:
	cd collectors; scrapy crawl glassdoor-job-interview -a query='data-scientist-interview-questions-SRCH_KO0,14.htm' -a max_items=5 -a search_kw='data scientist'

run_jupyter:
	jupyter lab