from django.http import HttpResponse
from django.views import View

class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello, World!</h1>")
