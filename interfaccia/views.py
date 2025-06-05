from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Ciao! Lorenzo Targon è proprio un frociazzo di merda!! xD</h1>")
