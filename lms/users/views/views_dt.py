from django.views.generic import TemplateView

class TestView(TemplateView):
    template_name = 'users/django_templates/index.html'
