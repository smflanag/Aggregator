from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def Homepage(request):
    template_name = 'home.html'
    return render(request, 'home.html')