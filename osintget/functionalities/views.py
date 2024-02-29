from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    return render(request , 'home.html')

def index(request):
    return render(request, 'index.html')

def iplocation(request):
    pass

def fraudEmail(request):
    pass

def phoneOSINT(request):
    pass

def fraudLink(request):
    pass


