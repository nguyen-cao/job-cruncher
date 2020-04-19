import numpy as np
import pandas as pd
import spacy
import en_core_web_md

nlp = en_core_web_md.load()

def process_text(text):
    doc = nlp(text)
    result = []
    for token in doc:
        if token.text in nlp.Defaults.stop_words:
            continue
        if token.is_punct:
            continue
        if token.lemma_ == '-PRON-':
            continue
        result.append(token.text)
    return " ".join(result)