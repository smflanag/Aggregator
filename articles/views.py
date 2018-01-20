from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView


def Homepage(request):
    template_name = 'home.html'
    return render(request, 'home.html')

class LoggedInView(LoginRequiredMixin,TemplateView):
    template_name = 'users_only.html'

    def get(self, request):
        return self.render_to_response({})