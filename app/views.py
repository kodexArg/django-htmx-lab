from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from random import randint


class Home(TemplateView):
    template_name = "index.html"
