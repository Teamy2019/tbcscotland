from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    return HttpResponse("Welcome to TBCScotland")


def search(request):

    return HttpResponse("Welcome to TBCScotland/search")


def about(request):

    return HttpResponse("Welcome to TBCScotland/about")


def getstarted(request):

    return HttpResponse("Welcome to TBCScotland/getstarted")


def profiles(request):

    return HttpResponse("Welcome to TBCScotland/profiles")


def lendandsell(request):

    return HttpResponse("Welcome to TBCScotland/lendandsell")


def projects(request):

    return HttpResponse("Welcome to TBCScotland/projects")


def services(request):

    return HttpResponse("Welcome to TBCScotland/services")


def login(request):

    return HttpResponse("Welcome to TBCScotland/login")


def signup(request):
    return HttpResponse("Welcome to TBCScotland/signup")









