from sys import exit

from sqlalchemy.orm.exc import NoResultFound
from flask.cli import AppGroup
import click
from urllib.parse import urlencode

from collectors.manage import CrawlerManager

manager = AppGroup(help="Company review management commands.")
CRAWLERS = {
    'indeed': 'indeed-company-review',
}

@manager.command()
@click.argument('name')
@click.option("--company", "company", default="air canada", help="Company to look for reviews")
@click.option(
    "--location",
    "location",
    default="CA",
    help="Location for reviewers",
)
@click.option(
    "--max_items",
    "max_items",
    default=5,
    help="Number returned reviews",
)
@click.option("--query", "query", default=None, help="Query to crawl reviews")
def crawl(name='indeed', company='air canada', location='CA', max_items=5, query=None):
    print("Crawl site (%s)..." % (name))
    crawler_name = CRAWLERS.get(name)
    if crawler_name != None:
        print("Crawler (%s)..." % (name))
        crawlerMgr = CrawlerManager()
        params = {}
        if name == 'indeed':
            params = {'lang':'en','fcountry':location}

        company_name = '-'.join(company.title().split())
        if query == None:    
            query = '{}/reviews?{}'.format(company_name, urlencode(params))
        crawlerMgr.start(crawler_name, query=query, max_items=max_items, company=company.title())