from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tbc.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from tbc.models import LendAndSell
from tbc.models import Projects
from tbc.models import Service
from tbc.models import Profile


# Create your views here.


def home(request):

    context_dict = {}
    return render(request, 'tbc/home.html', context=context_dict)


def search(request):

    context_dict = {}
    return render(request, 'tbc/search.html', context=context_dict)


def about(request):

    context_dict = {}
    return render(request, 'tbc/about.html', context=context_dict)


def getstarted(request):

    context_dict = {'boldmessage': "How to get started at TBCScotland!"}
    return render(request, 'tbc/getstarted.html', context=context_dict)


def profiles(request):

    profiles_list = Profile.objects.order_by('-views')[:20]

    context_dict = {'profiles': profiles_list}

    return render(request, 'tbc/profiles.html', context=context_dict)

def show_profile(request, profile_name_slug):
    context_dict = {}

    try:
        profile = Profile.objects.get(slug=profile_name_slug)
        context_dict['profile'] = profile
    except Profile.DoesNotExist:
        context_dict['profile'] = None

    return render(request, 'tbc/profile.html', context_dict)

def lendandsell(request):

    lend_and_sell_list = LendAndSell.objects.order_by('views')[:20]
    context_dict = {'lend_and_sell': lend_and_sell_list}

    return render(request, 'tbc/lendandsell.html', context_dict)

#One instance of an ad here:
def show_lendandsell(request, lendandsell_name_slug):
    context_dict = {}

    try:
        lendandsell = LendAndSell.objects.get(slug=lendandsell_name_slug)
        context_dict['lend_ad'] = lendandsell
    except LendAndSell.DoesNotExist:
        context_dict['lend_ad'] = None

    return render(request, 'tbc/lendandsellad.html', context_dict)


def projects(request):

    projects_list = Projects.objects.order_by('views')[:20]
    context_dict = {'projects': projects_list}

    return render(request, 'tbc/projects.html', context_dict)

def show_project(request, project_name_slug):
    context_dict = {}

    try:
        project = Projects.objects.get(slug=project_name_slug)
        context_dict['project_ad'] = project
    except Projects.DoesNotExist:
        context_dict['project_ad'] = None
    
    return render(request, 'tbc/projectad.html', context_dict)


def services(request):

    service = Service.objects.order_by('views')[:20]
    context_dict ={'services': service}

    return render(request, 'tbc/services.html', context_dict)

def show_service(request, service_name_slug):
    context_dict = {}

    try:
        service = Service.objects.get(slug=service_name_slug)
        context_dict['service_ad'] = service
    except Service.DoesNotExist:
        context_dict['service_ad'] = None
    
    return render(request, 'tbc/servicead.html', context_dict)


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
