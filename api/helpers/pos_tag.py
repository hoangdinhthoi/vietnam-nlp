from api.helpers.text_preprocess import PreprocessText
from api.helpers.text_preprocess import FeaturizeTextPosTagger
from api.helpers.text_preprocess import FeaturizeText
from api import pos_tagger
from api.helpers.sentence_tokenize import SentenceTokenize


class PosTagger:
    @staticmethod
    def pos_tag(sentence):
        sentence = SentenceTokenize.tokenize(sentence)
        sentence = FeaturizeText.sylabelize(sentence)
        feature = FeaturizeTextPosTagger.sentence2features(sentence)
        labels = pos_tagger.tag(feature)
        sent = [s[0] for s in sentence]
        return [sent, labels]
