from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    return render(request , 'home.html')

def index(request):
    return render(request, 'index.html')


def fraudEmail(request):
    
    return render(request, 'fmaildet.html')

def phoneOSINT(request):
    pass

def fraudLink(request):
    pass


