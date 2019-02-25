from django.urls import path
from api.views.sentence_tokenize_view import SentenceTokenizeView
from api.views.pos_view import PosTagView

app_name = 'api'
urlpatterns = [
    path('sentence_tokenize', SentenceTokenizeView.as_view(), name='sentence tokenize'),
    path('pos_tag', PosTagView.as_view(), name='part of speech tag')
]
