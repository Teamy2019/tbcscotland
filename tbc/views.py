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
from tbc.forms import LendAndSellForm, ServiceForm, ProjectForm
from django.db.models import Q
from datetime import datetime

# Create your views here.


def home(request):
    # Line added to test cookies.
    request.session.set_test_cookie()

    # context_dict = {}
    return render(request, 'tbc/home.html')


def search(request):

    context_dict = {}
    query = request.GET.get('q')

    resultsLend = LendAndSell.objects.filter(Q(title__icontains=query) | Q(keywords__icontains=query))
    resultsProject = Projects.objects.filter(Q(title__icontains=query) | Q(keywords__icontains=query))
    resultsService = Service.objects.filter(Q(title__icontains=query) | Q(keywords__icontains=query))
    context_dict = {'resultsLend': resultsLend, 'resultsProject': resultsProject, 'resultsService': resultsService}
    return render(request, 'tbc/search.html', context_dict)


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

    # Lines added for cookie testing
    if request.session.test_cookie_worked():
        print("TEST: cookies functional...")
        request.session.delete_test_cookie()


    context_dict = {}

    try:
        profile = Profile.objects.get(slug=profile_name_slug)
        context_dict['profile'] = profile

        query = profile
        print(query)

        resultsLend = LendAndSell.objects.filter(profile=query)
        resultsProject = Projects.objects.filter(profile=query)
        resultsService = Service.objects.filter(profile=query)
        visitor_cookie_handler(request)
        context_dict['resultsLend'] = resultsLend
        context_dict['resultsProject'] = resultsProject
        context_dict['resultsService'] = resultsService
        context_dict['visits'] = request.session['visits']

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

@login_required
def post_lendAndSell(request):

    if request.method == 'POST':

        lendAndSell_form = LendAndSellForm(data=request.POST)
        # added for testing - <<retrieve type of form from request objectprint>> (request.POST)

        if lendAndSell_form.is_valid():
            lendandsell = lendAndSell_form.save()
            lendandsell.save()
            context_dict = {'ad_slug': lendandsell.slug, 'category': "lendandsell"}
            return ad_posted(request, context_dict)
        else:
            print(lendAndSell_form.errors)
    else:
        lendAndSell_form = LendAndSellForm()

    return render(request, 'tbc/postlendandsell.html', {'lendAndSell_form': lendAndSell_form})

def post_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(data=request.POST)
        if project_form.is_valid():
            project = project_form.save()
            project.save()
            context_dict = {'ad_slug': project.slug, 'category': "projects"}
            return ad_posted(request, context_dict)

        else:
            print(project_form.errors)
    else:
        project_form = ProjectForm()

    return render(request, 'tbc/postproject.html', {'project_form': project_form})

def post_service(request):
    if request.method == 'POST':
        service_form = ServiceForm(data=request.POST)
        if service_form.is_valid():
            service = service_form.save()
            service.save()
            context_dict = {'ad_slug': service.slug, 'category': "services"}
            return ad_posted(request, context_dict)
        else:
            print(service_form.errors)
    else:
        service_form = ServiceForm()
    return render(request, 'tbc/postservice.html', {'service_form': service_form})

def post_ad(request):

    if request.method == 'POST':
        print("Hello world")
        #Do some stuff
    else:
        lendAndSell_form = LendAndSellForm()
        project_form = ProjectForm()
        service_form = ServiceForm()

    return render(request, 'tbc/postad.html', {'lendAndSell_form': lendAndSell_form, 'project_form': project_form, 'service_form': service_form})

def ad_posted(request, context_dict):
    return render(request, 'tbc/adposted.html', context_dict)

#def login(request):

    #context_dict = {'boldmessage': "Login to TBCScotland!"}
    #return render(request, 'TBCScotland/login.html', context=context_dict)

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


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    # Getting the number of visits to the site.

    visits = int(get_server_side_cookie(request, 'visits', '1'))

    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).seconds > 0:
        visits = visits + 1

        request.session['last_visit'] = str(datetime.now())
    else:
        # Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits
