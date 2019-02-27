from django.shortcuts import render
from django.http import HttpResponse
from tbc.forms import UserForm, UserProfileForm

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


def login(request):

    return HttpResponse("Welcome to TBCScotland/login")


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
