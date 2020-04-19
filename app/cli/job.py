from sys import exit

from flask.cli import AppGroup
import click
from urllib.parse import urlencode

from collectors.manage import CrawlerManager
from analysis import utils, job
from ml import occupation as occupation_scorer

manager = AppGroup(help="Job management commands.")
CRAWLERS = {
    'indeed': 'indeed-job-list',
    'glassdoor': 'glassdoor-job-list',
}

@manager.command()
@click.argument('name')
@click.option("--search_kw", "search_kw", default="data scientist", help="Keyword to search on the site")
@click.option(
    "--location",
    "location",
    default="Vancouver, BC",
    help="Location to search for job",
)
@click.option(
    "--max_items",
    "max_items",
    default=5,
    help="Number returned jobs",
)
@click.option("--query", "query", default=None, help="Query to crawl jobs")
def crawl(name='indeed', search_kw='data scientist', location='Vancouver, BC', max_items=5, query=None):
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


@manager.command()
@click.argument('name')
@click.option("--field", "field", default="description", help="Field to do analysis")
@click.option("--n_top", "n_top", default=20, help="Number top items to return")
@click.option("--search_kw", "search_kw", default="", help="search keyword for filtering")
@click.option("--is_saved", "is_saved", default=False, help="is saved or not")
def analyze(name, field='description', n_top=20, search_kw='', is_saved=False):
    if name == 'word':
        job.top_words(field, n_top=n_top, search_kw=search_kw, is_saved=is_saved)
    elif name == 'bigram':
        job.top_bigrams(field, n_top=n_top, search_kw=search_kw, is_saved=is_saved)
    elif name == 'trigram':
        job.top_trigrams(field, n_top=n_top, search_kw=search_kw, is_saved=is_saved)

@manager.command()
@click.argument('ngram_type')
@click.option("--k", "k", default=20, help="Number top ngrams")
@click.option("--data_table", "data_table", default="job_occupation", help="data table to store results")
def occupation_score(ngram_type, k=20, data_table='job_occupation'):
    table = '{0}_{1}_{2}'.format(data_table,ngram_type,k)
    occupation_scorer.score(ngram_type=ngram_type, k=k, data_table=table)