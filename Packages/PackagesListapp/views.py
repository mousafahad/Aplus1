from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HomePages(request):
    return render(request, 'HomePage/hp.html')

def Register(request):
    return render(request, 'account/register.html')

def Login(request):
    return render(request, 'account/login.html')
