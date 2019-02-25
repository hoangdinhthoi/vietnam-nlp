from api.views.abstract_api_view import AbstractAPIView
from django.utils.translation import gettext_lazy as _
from api.forms.sentence_tokenize_form import SentenceTokenizeForm
from api.helpers.pos_tag import PosTagger


class PosTagView(AbstractAPIView):
    success = _('Part of speech tag successfully.')
    failure = _('Part of speech tag fail.')

    def post(self, request):
        form = SentenceTokenizeForm(request.data)
        if not form.is_valid():
            return self.json_format(code=442, data=[], message=self.failure, errors=form.errors)
        sentence = form.cleaned_data.get('sentence')
        result = PosTagger.pos_tag(sentence)
        return self.json_format(code=200, data=result, message=self.success, errors=[])
