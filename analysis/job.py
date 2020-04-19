import pandas as pd
import re
import cufflinks as cf
from textblob import TextBlob
from sqlalchemy import create_engine

from analysis import utils

cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)

engine = create_engine(utils.DATABASE_URI, echo=False)

def top_words(field='description', stop_words='english', n_top=20, search_kw='', is_saved=False):
    query = 'select {} from job_post'
    if search_kw:
        query = 'select {}, search_kw from job_post'
    df = pd.read_sql_query(query.format(field),engine)
    if search_kw:
        common_words = utils.get_top_n_words(df[df['search_kw'] == search_kw][field], stop_words=stop_words, n=n_top)
    else:
        common_words = utils.get_top_n_words(df[field], stop_words=stop_words, n=n_top)
    ngrams = [(word[0], word[1], field, 1, search_kw) for word in common_words]
    df2 = pd.DataFrame(ngrams, columns = ['ngram' , 'count', 'field', 'type', 'search_kw'])
    if is_saved:
        df2.to_sql('job_ngram', con=engine, if_exists='append', index=False)
    return df2

def top_bigrams(field='description', stop_words='english', n_top=20, search_kw='', is_saved=False):
    query = 'select {} from job_post'
    if search_kw:
        query = 'select {}, search_kw from job_post'
    df = pd.read_sql_query(query.format(field),engine)
    if search_kw:
        common_words = utils.get_top_n_bigrams(df[df['search_kw'] == search_kw][field], stop_words=stop_words, n=n_top)
    else:
        common_words = utils.get_top_n_bigrams(df[field], stop_words=stop_words, n=n_top)
    ngrams = [(word[0], word[1], field, 2, search_kw) for word in common_words]
    df2 = pd.DataFrame(ngrams, columns = ['ngram' , 'count', 'field', 'type', 'search_kw'])
    if is_saved:
        df2.to_sql('job_ngram', con=engine, if_exists='append', index=False)
    return df2

def top_trigrams(field='description', stop_words='english', n_top=20, search_kw='', is_saved=False):
    query = 'select {} from job_post'
    if search_kw:
        query = 'select {}, search_kw from job_post'
    df = pd.read_sql_query(query.format(field),engine)
    if search_kw:
        common_words = utils.get_top_n_trigrams(df[df['search_kw'] == search_kw][field], stop_words=stop_words, n=n_top)
    else:
        common_words = utils.get_top_n_trigrams(df[field], stop_words=stop_words, n=n_top)
    ngrams = [(word[0], word[1], field, 2, search_kw) for word in common_words]
    df2 = pd.DataFrame(ngrams, columns = ['ngram' , 'count', 'field', 'type', 'search_kw'])
    if is_saved:
        df2.to_sql('job_ngram', con=engine, if_exists='append', index=False)
    return df2    



