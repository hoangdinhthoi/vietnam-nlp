import pickle
from vietnam_nlp.settings import VOCAB_BI_GRAM
from vietnam_nlp.settings import TOKEN_TAGGER_MODEL
import pycrfsuite


with open(VOCAB_BI_GRAM, 'rb') as f:
    vocab_bi_gram = pickle.load(f)

token_tagger = pycrfsuite.Tagger()
token_tagger.open(TOKEN_TAGGER_MODEL)
