import nltk
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import numpy as np
import translators as ts
import translators.server as tss

# check if punkt is installed, if not, install it
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    
# check if stopwords is installed, if not, install it
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
    
# check if wordnet is installed, if not, install it
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
    
# check if averaged_perceptron_tagger is installed, if not, install it
try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')
    
# load the synonyms dataframe
synonyms = pd.read_parquet('data/synonyms_pt_BR.parquet', engine='pyarrow')
    
# function to check the number of words in the synonyms dataframe
def check_synonyms():
    print('The synonyms dataframe has', len(synonyms), 'synonyms.')