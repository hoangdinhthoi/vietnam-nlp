from api.forms.abstract_form import AbstractForm
from django import forms


class SentenceTokenizeForm(AbstractForm):
    sentence = forms.CharField(required=True)
