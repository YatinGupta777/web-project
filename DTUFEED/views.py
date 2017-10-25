from django.views.generic import TemplateView

#Test and thanks redirect defined in settings.py file
class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name ='thanks.html'
