import numpy as np
import pandas as pd
import itertools
from ml import nlp, process_text
from analysis.job import engine, top_words, top_bigrams, top_trigrams
from models.onet import ONet_Manager

def score(ngram_type='bigram', k=20):
    query = 'select id, title, description from job_post'
    job_df = pd.read_sql_query(query, engine)
    job_titles = job_df['title'].to_list()
    job_titles = [title.lower() for title in job_titles]

    for i in range(len(job_titles)):
        job_titles[i] = process_text(job_titles[i])

    if ngram_type == 'word':
        vocab_df = top_words(field='description',n_top=k)
    elif ngram_type == 'bigram':
        vocab_df = top_bigrams(field='description',n_top=k)
    elif ngram_type == 'trigram':
        vocab_df = top_trigrams(field='description',n_top=k)

    top_ngrams = vocab_df['ngram'].unique()

    job_title_df = job_df.copy()
    job_title_df['title_processed'] = job_titles
    job_title_df['keyword_processed'] = job_title_df.apply(lambda row: [ngram for ngram in top_ngrams if ngram in row.description], axis=1)
    job_title_df['title_processed'] = job_title_df.apply(lambda row: '{} {}'.format(row.title_processed, ' '.join(row.keyword_processed)), axis=1)

    occupation_df = ONet_Manager.occupations()
    occupation_titles =  occupation_df['titles'].to_list()
    for i in range(len(occupation_titles)):
        occupation_titles[i] = [process_text(title.lower()) for title in occupation_titles[i].split(',')]
    occupation_df['titles_processed'] = occupation_titles

    df1 = job_title_df[['id', 'title', 'title_processed']]
    df2 = occupation_df[['identifier', 'titles_processed']]

    df_vals = list(itertools.product(df1.values.tolist(),df2.values.tolist()))
    colnames = list(df1.columns) + list(df2.columns)
    score_df = pd.DataFrame(list(map(lambda x : sum(x,[]), df_vals)), columns=colnames)
    nlp_title = np.array([nlp(title) for title in df1['title_processed']])
    nlp_occupation_title = np.array([nlp(' '.join(title)) for title in df2['titles_processed']])
    scores = np.array([title.similarity(occupation_title) \
                    for title in nlp_title \
                    for occupation_title in nlp_occupation_title])
    score_df['score'] = scores
    score_df = score_df.sort_values('score', ascending=False).drop_duplicates(['id'])
    score_df = score_df.sort_values('id')

    df1 = score_df.drop(['titles_processed', 'title_processed'], axis=1)
    df2 = occupation_df[['identifier', 'name']].drop_duplicates()

    job_occupation_scorer = df1.merge(df2, on='identifier', how='left')
    job_occupation_scorer.rename(columns={
        'id': 'job_id',
        'title':'job_title',
        'identifier': 'onet_identifier',
        'name':'occupation'
    }, inplace=True)

    job_occupation_scorer.to_sql('job_occupation', con=engine, if_exists='replace', index=False)