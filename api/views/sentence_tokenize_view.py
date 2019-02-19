from api.views.abstract_api_view import AbstractAPIView
from django.utils.translation import gettext_lazy as _
from api.forms.sentence_tokenize_form import SentenceTokenizeForm
from api.helpers.sentence_tokenize import SentenceTokenize


class SentenceTokenizeView(AbstractAPIView):
    success = _('Sentence tokenize successfully.')
    failure = _('Sentence tokenize fail.')

    def post(self, request):
        form = SentenceTokenizeForm(request.data)
        if not form.is_valid():
            return self.json_format(code=442, data=[], message=self.failure, errors=form.errors)
        sentence = form.cleaned_data.get('sentence')
        result = SentenceTokenize.tokenize(sentence)
        return self.json_format(code=200, data=result, message=self.success, errors=[])
