from api.helpers.text_preprocess import PreprocessText
from api.helpers.text_preprocess import FeaturizeTextNerTagger
from api.helpers.text_preprocess import FeaturizeText
from api import ner_tagger
from api.helpers.sentence_tokenize import SentenceTokenize


class NerTagger:
    @staticmethod
    def ner_tag(sentence):
        sentence = SentenceTokenize.tokenize(sentence)
        sentence = FeaturizeText.sylabelize(sentence)
        feature = FeaturizeTextNerTagger.sentence2features(sentence)
        labels = ner_tagger.tag(feature)
        sent = [s[0] for s in sentence]
        return [sent, labels]
        return None
