from api.helpers.text_preprocess import PreprocessText, FeaturizeText
from api import token_tagger


class SentenceTokenize:
    @staticmethod
    def tokenize(sentence):
        sentence = PreprocessText.replace_special_characters(sentence)
        sentence = FeaturizeText.sylabelize(sentence)
        feature = FeaturizeText.sentence2features(sentence)
        labels = token_tagger.tag(feature)
        result = ''
        for index, word in enumerate(sentence):
            if(labels[index] == 'I'):
                result += '_' + word[0]
            else:
                result += ' ' + word[0]
        return result
