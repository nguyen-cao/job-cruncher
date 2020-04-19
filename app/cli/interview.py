from sys import exit

from sqlalchemy.orm.exc import NoResultFound
from flask.cli import AppGroup
import click
from urllib.parse import urlencode

from collectors.manage import CrawlerManager

manager = AppGroup(help="Job interview management commands.")
CRAWLERS = {
    'glassdoor': 'glassdoor-job-interview',
}

@manager.command()
@click.argument('name')
@click.option("--search_kw", "search_kw", default="data scientist", help="Keyword to search on the site")
@click.option(
    "--location",
    "location",
    default="Vancouver, BC",
    help="Location to search for job interviews",
)
@click.option(
    "--max_items",
    "max_items",
    default=5,
    help="Number returned job interviews",
)
@click.option("--query", "query", default=None, help="Query to crawl job interviews")
def crawl(name='glassdoor', search_kw='data scientist', location='Vancouver, BC', max_items=5, query=None):
    print("Crawl site (%s)..." % (name))
    crawler_name = CRAWLERS.get(name)
    if crawler_name != None:
        print("Crawler (%s)..." % (name))
        crawlerMgr = CrawlerManager()
        params = {}
        if name == 'indeed':
            params = {'q':search_kw,'l':location}

        if query == None:    
            query = urlencode(params)
        crawlerMgr.start(crawler_name, query=query, max_items=max_items, search_kw=search_kw)