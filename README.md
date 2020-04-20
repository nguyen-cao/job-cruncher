# Job Market Analysis

Big data science project to automatically find out what skills would be in a job post.

## Installation
The following installation is on Ubuntu 18.04

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

Structure
----------
- [algorithms/](skills_ml/algorithms/) - Core algorithmic module. Each submodule is meant to contain a different type of component, such as a job title normalizer or a skill tagger, with a common interface so different pipelines can try out different versions of the components.
- [datasets/](skills_ml/datasets/) - Wrappers for interfacing with different datasets, such as ONET, Urbanized Area.
- [evaluation/](skills_ml/evaluation/) - Code for testing different components against each other.


Contributors
----------
- Kwame Porter Robinson - [Github](https://github.com/robinsonkwame)
- Eddie Lin - [Github](https://github.com/tweddielin)
- Tristan Crockett - [Github](https://github.com/thcrock)
- Zoo Chai - [Github](https://github.com/zoochai)
