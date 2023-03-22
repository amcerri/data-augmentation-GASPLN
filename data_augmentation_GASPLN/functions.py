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
synonyms = pd.read_parquet('data_augmentation_GASPLN/data/synonyms_pt_BR.parquet', engine='pyarrow')

def synonyms_replacement(text, df, percentage=0.5):
    tokens = nltk.word_tokenize(text)
    stop_words = nltk.corpus.stopwords.words('portuguese')
    
    number_of_words = int(len(tokens) * percentage)
    indexes = np.random.choice(len(tokens), number_of_words, replace=False)
    
    for index in indexes:
        word = tokens[index]
        
        if word not in df['word'].values:
            continue
        
        if word in stop_words:
            continue
        
        synonyms = list(df[df['word'] == word]['synonyms'].values[0])
        
        if len(synonyms) == 0:
            continue
        
        synonym_index = np.random.randint(0, len(synonyms))
        tokens[index] = synonyms[synonym_index]
        
    return ' '.join(tokens)

def back_translation(sentence, num_of_translations=2):
    first_translation = ts.translate_text(sentence, translator='google', to_language='es')
    second_translation = ts.translate_text(first_translation, translator='google', to_language='en')
    back_translation = ts.translate_text(second_translation, translator='google', to_language='pt')
    
    return back_translation