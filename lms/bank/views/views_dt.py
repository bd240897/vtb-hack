from django.views.generic import TemplateView

class TestView(TemplateView):
    template_name = 'bank/django_templates/index.html'
