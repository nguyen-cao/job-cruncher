# Job Market Analysis

Big data science project to automatically find out what skills would be in a job post.

Features
----------
- Collect job posts from job portals like Indeed.com, Glassdoor.ca
- Analyze job posts by open-source NLP and ML libraries like spaCy, Scikit-learn.
- Visualize results with Redash, an open-source business intelligence system.

This project is built based on the Docker containers, so it is easy to deploy to a distributed production environment for handling large-scale processing.

Structure
----------
- [collectors/](collectors/) - Data collection module is structured based on a typical Scrapy project. In its submodules you will find out several web spiders to scrape job posts, company reviews and job interviews from Indeed and Glassdoor.
- [models/](models/) - Data model module defines job and occupation models. This module serves as basis for other modules and in charge of storing data into Postgres database.
- [analysis/](analysis/) - Data analysis module is responsible for EDA tasks. There is a submodule [notebooks](analysis/notebooks/) contains various Jupyter Notebooks for job and occupation analysis. 
- [ml/](ml/) - Data mining module performs occupation scoring and competency scoring.
- [datasets/](datasets/) - Sample datasets of job posts, company reviews, job interviews and ONET database.
- [results/](results/) - This folder contains some intermediate results in CSV format used by other modules.
- [ui/](ui/) - Data visualization module is responsible for setting up Redash dashboards.
- [app/](app/) - Main app module is responsible for monitoring other modules to work with each other. This module is also in charge of setting up command lines to run tasks.

## Installation
The the following section, you will install different libraries and systems to run on Ubuntu 18.04

### Install Python 3.7
1. sudo apt update
2. sudo apt install software-properties-common
3. sudo add-apt-repository ppa:deadsnakes/ppa
4. sudo apt install python3.7
5. sudo apt install python3.7-dev
6. sudo apt install python3.7-venv

### Install Docker
1. sudo apt-get update
2. sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
2. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
3. sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
4. sudo apt-get install docker-ce docker-ce-cli containerd.io
5. sudo usermod -aG docker ${USER}

### Install Docker Compose
1. sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
2. sudo chmod +x /usr/local/bin/docker-compose


### Build from source code
1. git clone https://github.com/data-catalysis/job-cruncher.git
2. cd job-cruncher
3. python3.7 -m venv .venv
4. source .venv/bin/activate
5. pip install -r requirements.txt
6. make init_systems
7. make build_systems
8. make build_app

### Run
1. source .venv/bin/activate
2. make start_app

Examples
----------

**Example 1:** Crawl job posts from Indeed with data scientist as a search keyword. Also crawl maximum 50 posts from Vancouver, BC.

    python manage.py job crawl indeed --search_kw 'data scientist' --location 'Vancouver, BC' --max_items 50

**Example 2:** Crawl job posts from Glassdoor with data engineer as a search keyword. Also crawl maximum 100 posts from Toronto, ON.

    python manage.py job crawl glassdoor --search_kw 'data engineer’ --location Toronto, ON' --max_items 100 --query toronto-data-engineer-jobs-SRCH_IL.0,7_IC2281069_KO8,21.htm

**Example 3:** Analyze job posts to get the top 50 frequent bigrams.

    python manage.py job analyze bigram --n_top 50

**Example 4:** Compute the matching occupations of job posts using top 50 frequent bigrams.

    python manage.py job occupation-score bigram --k 50 --data_table 'job_occupation'

**Web Frontend:**
- URL: http://ec2-107-23-250-99.compute-1.amazonaws.com/
- Credential to login: Email : cmpt733@sfu.ca | Password: cmpt733

**Public Dashboards:**
- [Job Post Analysis](http://ec2-107-23-250-99.compute-1.amazonaws.com/public/dashboards/095dLWQZM89cZScGVkrwR2cacnYCAS2kRaPh63sU?org_slug=default)
- [Job Occupation Scoring](http://ec2-107-23-250-99.compute-1.amazonaws.com/public/dashboards/AkliuppeebHAzXaC8A7pFlN9NCD15vUK2HAbuYe2?org_slug=default)


Contributors
----------
- Nguyen Cao - [Github](https://github.com/data-catalysis)
- Madana Krishnan K. V. - [Github](https://github.com/MadanKrishnan97)
- Sanjana R. Chauhan - [Github](https://github.com/Sanjana12111994)
- Sumukha B. Balasubramanya - [Github](https://github.com/sumukhab)
