from django.urls import path
from api.views.sentence_tokenize_view import SentenceTokenizeView


app_name = 'api'
urlpatterns = [
    path('sentence_tokenize', SentenceTokenizeView.as_view(), name='sentence tokenize'),
]
