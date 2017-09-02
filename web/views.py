from django.shortcuts import render
from . import templates
from django.http import HttpResponse
def login(request):
    return render(request, 'login.html', {})
def signup(request):
    return render(request, 'signup.html', {})
def index(request):
    return render(request,'index.html',{})
def introduction(request):
    return render(request, 'introduction.html', {})
def team(request):
    return render(request, 'team.html', {})
def download(request):
    return render(request,'download.html',{})
def contact(request):
    return render(request, 'contact.html', {})
def user(request):
    return render(request, 'user.html', {})


