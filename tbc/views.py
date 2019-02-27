from django.shortcuts import render
from django.http import HttpResponse
from tbc.forms import UserForm, UserProfileForm
from tbc.models import LendAndSell
from tbc.models import Projects
from tbc.models import Service
from tbc.models import Profile

# Create your views here.


def home(request):

    context_dict = {}
    return render(request, 'TBCScotland/home.html', context=context_dict)


def search(request):

    context_dict = {}
    return render(request, 'TBCScotland/search.html', context=context_dict)


def about(request):

    context_dict = {}
    return render(request, 'TBCScotland/about.html', context=context_dict)


def getstarted(request):

    context_dict = {'boldmessage': "How to get started at TBCScotland!"}
    return render(request, 'TBCScotland/getstarted.html', context=context_dict)


def profiles(request):

    profiles_list = Profile.objects.order_by('-views')[:20]

    context_dict = {'profiles': profiles_list}

    return render(request, 'TBCScotland/profiles.html', context=context_dict)


def lendandsell(request, lend_and_sell_slug):

    try:

        context_dict = {}
        lend_and_sell = LendAndSell.objects.get(slug=lend_and_sell_slug)
        context_dict['lend_and_sell'] = lend_and_sell

    except LendAndSell.DoesNotExist:

        context_dict['lend_and_sell'] = None

    return render(request, 'TBCScotland/lendandsell.html', context_dict)


def projects(request, projects_slug):

    try:

        context_dict = {}
        lend_and_sell = Projects.objects.get(slug=projects_slug)
        context_dict['projects_slug'] = lend_and_sell

    except Projects.DoesNotExist:

        context_dict['projects'] = None

    return render(request, 'TBCScotland/projects.html', context_dict)


def services(request, services_slug):

    try:

        context_dict = {}
        service = Service.objects.get(slug=services_slug)
        context_dict['service'] = service

    except Service.DoesNotExist:

        context_dict['service'] = None

    return render(request, 'TBCScotland/services.html', context_dict)


def login(request):

    context_dict = {'boldmessage': "Login to TBCScotland!"}
    return render(request, 'TBCScotland/login.html', context=context_dict)


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
