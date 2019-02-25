import unicodedata as ud
from api import vocab_bi_gram
from api import filtered_tags
import re


class FeaturizeText:
    @staticmethod
    def word2features(sentence, i):
        word = sentence[i][0]
        # feature of the current word
        features = {
            'bias': 1.0,
            'word.lower()': word.lower(),
            'word.isupper()': word.isupper(),
            'word.istitle()': word.istitle(),
            'word.isdigit()': word.isdigit(),
        }
        if i > 0:
            word1 = sentence[i - 1][0]
            # feature of the word before the current word
            features.update({
                '-1:word.lower()': word1.lower(),
                '-1:word.istitle()': word1.istitle(),
                '-1:word.isupper()': word1.isupper(),
                '-1:word.isdigit()': word1.isdigit(),
                '-1:word.bi_gram()': ' '.join([word1, word]).lower() in vocab_bi_gram,
            })
            if i > 1:
                word2 = sentence[i - 2][0]
                # feature of the word before the word before the current word
                features.update({
                    '-2:word.lower()': word2.lower(),
                    '-2:word.istitle()': word2.istitle(),
                    '-2:word.isupper()': word2.isupper(),
                    '-2:word.isdigit()': word2.isdigit(),
                })

        if i < len(sentence) - 1:
            word1 = sentence[i + 1][0]
            # feature of the word after the current word
            features.update({
                '+1:word.lower()': word1.lower(),
                '+1:word.istitle()': word1.istitle(),
                '+1:word.isupper()': word1.isupper(),
                '+1:word.isdigit()': word1.isdigit(),
                '+1:word.bi_gram()': ' '.join([word, word1]).lower() in vocab_bi_gram,
            })
            if i < len(sentence) - 2:
                word2 = sentence[i + 2][0]
                # feature of the word after the word after the current word
                features.update({
                    '+2:word.lower()': word2.lower(),
                    '+2:word.istitle()': word2.istitle(),
                    '+2:word.isupper()': word2.isupper(),
                    '+2:word.isdigit()': word2.isdigit(),
                })
        return features

    @staticmethod
    def sentence2features(sentence):
        return [FeaturizeText.word2features(sentence, i) for i in range(len(sentence))]

    @staticmethod
    def sylabelize(sentence):
        email = '([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+).([a-zA-Z0-9-.]+)'
        url = 'https?:\/\/[^\s]*'
        datetime = '(\d+)\s?([/:-])\s?(\d+)\s?([/:-])\s?(\d+)'
        specials = ['==>', '->', '\.\.\.', '>>']
        digit = '\d+([\.,]\d+)+'
        fraction = '\d+\/\d+'
        percent = "\d+([.,]\d+)?%"
        name3 = '([A-Z][^0-9\s,.]+)\s([A-Z][^0-9\s,.]+)\s([A-Z][^0-9\s,.]+)'
        name2 = '([A-Z][^0-9\s,.]+)\s([A-Z][^0-9\s,.]+)'
        word = '\w+[_-]?\w*'
        non_word = '[^\w\s]'
        abbreviations = [
            '[A-ZĐ]+\.',
            'Tp\.',
            'Mr\.', 'Mrs\.', 'Ms\.',
            'Dr\.', 'ThS\.'
        ]
        sentence = ud.normalize('NFC', sentence)
        patterns = []
        patterns.extend(abbreviations)
        patterns.extend(specials)
        patterns.extend([email, url])
        patterns.extend([datetime])
        patterns.extend([name3, name2])
        patterns.extend([percent, digit, fraction, non_word, word])
        patterns = "(" + "|".join(patterns) + ")"
        tokens = re.findall(patterns, sentence, re.UNICODE)
        return [(token[0],) for token in tokens]


class PreprocessText:
    @staticmethod
    def replace_special_characters(sentence):
        sentence = sentence.replace('”', '"')
        sentence = sentence.replace('“', '"')
        sentence = sentence.replace('…', '...')
        sentence = sentence.replace('’', '\'')
        return sentence


class FeaturizeTextPosTagger(FeaturizeText):
    @staticmethod
    def word2features(sentence, i):
        word = sentence[i][0]
        features = {
            'bias': 1.0,
            'word.lower()': word.lower(),
            'word.istitle()': word.istitle(),
            'word.isdigit()': word.isdigit(),
            'word[:1].isdigit()': word[:1].isdigit(),
            'word[:3].isupper()': word[:3].isupper(),
            'word.isfiltered': word in filtered_tags,
        }
        if i > 0:
            word1 = sentence[i-1][0]
            features.update({
                '-1:word.lower()': word1.lower(),
                '-1:word.istitle()': word1.istitle(),
                '-1:word[:1].isdigit()': word1[:1].isdigit(),
                '-1:word[:3].isupper()': word1[:3].isupper(),
            })
            if i > 1:
                word2 = sentence[i-2][0]
                features.update({
                    '-2:word.lower()': word2.lower(),
                    '-2:word.istitle()': word2.istitle(),
                    '-2:word.isupper()': word2.isupper(),
                })
        else:
            features['BOS'] = True
        if i < len(sentence) - 1:
            word1 = sentence[i+1][0]
            features.update({
                '+1:word.lower()': word1.lower(),
                '+1:word.istitle()': word1.istitle(),
                '+1:word[:1].isdigit()': word1[:1].isdigit(),
                '+1:word.isupper()': word1.isupper(),
            })
            if i < len(sentence) - 2:
                word2 = sentence[i+2][0]
                features.update({
                    '+2:word.lower()': word2.lower(),
                    '+2:word.istitle()': word2.istitle(),
                    '+2:word.isupper()': word2.isupper(),
                })
        else:
            features['EOS'] = True
        return features
