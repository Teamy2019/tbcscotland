from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tbc.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):

    return render(request, 'tbc/home.html')


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


def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'tbc/signup.html', {'user_form': user_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("The account has been disabled")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'tbc/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
