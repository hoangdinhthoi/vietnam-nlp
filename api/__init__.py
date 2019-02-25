import pickle
from vietnam_nlp.settings import VOCAB_BI_GRAM
from vietnam_nlp.settings import TOKEN_TAGGER_MODEL
from vietnam_nlp.settings import POS_TAGGER_MODEL
import pycrfsuite
import string


with open(VOCAB_BI_GRAM, 'rb') as f:
    vocab_bi_gram = pickle.load(f)

token_tagger = pycrfsuite.Tagger()
token_tagger.open(TOKEN_TAGGER_MODEL)

pos_tagger = pycrfsuite.Tagger()
pos_tagger.open(POS_TAGGER_MODEL)

filtered_tags = set(string.punctuation)
filtered_tags.add(u'\u2026')
filtered_tags.add(u'\u201d')
filtered_tags.add(u'\u201c')
filtered_tags.add(u'\u2019')
filtered_tags.add('...')
