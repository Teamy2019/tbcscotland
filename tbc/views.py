from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from tbc.forms import ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from tbc.models import LendAndSell
from tbc.models import Projects
from tbc.models import Service
from tbc.models import Profile
from tbc.models import Comments
from tbc.forms import LendAndSellForm, ServiceForm, ProjectForm, CommentsForm, ContactForm, UserForm
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError




def home(request):
    # Line added to test cookies.
    request.session.set_test_cookie()
    profiles_list = Profile.objects.order_by('-views')[:6]
    lends_list = LendAndSell.objects.order_by('-views')[:2]
    project_list = Projects.objects.order_by('-views')[:2]
    service_list = Service.objects.order_by('-views')[:2]

    context_dict = {'profiles_list': profiles_list, 'lends_list':lends_list, 'project_list': project_list, 'service_list': service_list}
    return render(request, 'tbc/home.html', context_dict)


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

    profiles_list = Profile.objects.all().order_by('-views')
    paginator = Paginator(profiles_list, 8)

    page = request.GET.get('page', 1)
    profiles = paginator.page(page)

    context_dict = {'profiles': profiles}

    return render(request, 'tbc/profiles.html', context_dict)


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

        visitor_cookie_handler(request)
        context_dict['visits'] = request.session['visits']

        profile.views += 1
        profile.save()
        comments = Comments.objects.filter(profile=profile)
        resultsLend = LendAndSell.objects.filter(profile=query)
        resultsProject = Projects.objects.filter(profile=query)
        resultsService = Service.objects.filter(profile=query)
        context_dict['resultsLend'] = resultsLend
        context_dict['resultsProject'] = resultsProject
        context_dict['resultsService'] = resultsService
        context_dict['comments'] = comments
        context_dict['comment_form'] = CommentsForm()
        context_dict['contact_form'] = ContactForm()

        if request.method == 'POST':
            if 'btncomment' in request.POST:
                comment_form = CommentsForm(data=request.POST)

                if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.author = request.user
                    comment.profile = profile
                    comment.save()
                else:
                    print(comment_form.errors)

            elif 'btncontact' in request.POST:
                contact_form = ContactForm(data=request.POST)
                if contact_form.is_valid():
                    from_email = request.user.email
                    to_email = profile.user.email
                    subject = contact_form.cleaned_data['subject']
                    message = contact_form.cleaned_data['message']
                    try:
                        send_mail(subject, message, from_email, [to_email])
                    except BadHeaderError:
                        return HttpResponse('Invalid header found')

                else:
                    contact_form = ContactForm()

    except Profile.DoesNotExist:
        context_dict['profile'] = None

    return render(request, 'tbc/profile.html', context_dict)

def lendandsell(request):

    lend_and_sell_list = LendAndSell.objects.all().order_by('views')
    paginator = Paginator(lend_and_sell_list, 8)

    page = request.GET.get('page', 1)
    lendandsell = paginator.page(page)

    context_dict = {'lend_and_sell': lendandsell}

    return render(request, 'tbc/lendandsell.html', context_dict)


def show_lendandsell(request, lendandsell_name_slug):
    context_dict = {}

    try:
        lendandsell = LendAndSell.objects.get(slug=lendandsell_name_slug)
        comments = Comments.objects.filter(lendandsell=lendandsell)
        profile = Profile.objects.get(username=lendandsell.profile)
        context_dict['lend_ad'] = lendandsell
        context_dict['comments'] = comments
        context_dict['comment_form'] = CommentsForm()
        context_dict['profile'] = profile

        if request.method == 'POST':
            comment_form = CommentsForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.lendandsell = lendandsell
                comment.save()
            else:
                print(comment_form.errors)


    except LendAndSell.DoesNotExist:
        context_dict['lend_ad'] = None

    return render(request, 'tbc/lendandsellad.html', context_dict)


def projects(request):

    projects_list = Projects.objects.all().order_by('views')
    paginator = Paginator(projects_list, 8)

    page = request.GET.get('page', 1)
    projects = paginator.page(page)

    context_dict = {'projects': projects}

    return render(request, 'tbc/projects.html', context_dict)


def show_project(request, project_name_slug):
    context_dict = {}

    try:
        project = Projects.objects.get(slug=project_name_slug)
        comments = Comments.objects.filter(project=project)
        profile = Profile.objects.get(username=project.profile)
        context_dict['project_ad'] = project
        context_dict['comments']= comments
        context_dict['comment_form'] = CommentsForm()
        context_dict['profile'] = profile
        if request.method == 'POST':
            comment_form = CommentsForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.project = project
                comment.save()
            else:
                print(comment_form.errors)

    except Projects.DoesNotExist:
        context_dict['project_ad'] = None

    return render(request, 'tbc/projectad.html', context_dict)


def services(request):

    service_list = Service.objects.all().order_by('views')
    paginator = Paginator(service_list, 8)

    page = request.GET.get('page', 1)
    service = paginator.page(page)

    context_dict ={'services': service}

    return render(request, 'tbc/services.html', context_dict)


def show_service(request, service_name_slug):
    context_dict = {}

    try:
        service = Service.objects.get(slug=service_name_slug)
        comments = Comments.objects.filter(service=service)
        profile = Profile.objects.get(username=service.profile)
        context_dict['comments'] = comments
        context_dict['service_ad'] = service
        context_dict['comment_form'] = CommentsForm()
        context_dict['profile'] = profile
        if request.method == 'POST':
            comment_form = CommentsForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.service = service
                comment.save()
            else:
                print(comment_form.errors)

    except Service.DoesNotExist:
        context_dict['service_ad'] = None

    return render(request, 'tbc/servicead.html', context_dict)

@login_required
def post_lendAndSell(request):

    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        lend = LendAndSell.objects.get_or_create(title=request.POST.get('title'), profile=profile)[0]
        lend.description = request.POST.get('description')
        lend.price = request.POST.get('price')
        lend.availability = request.POST.get('availability')
        lend.keywords = request.POST.get('keywords')

        if 'uploadpicture' in request.FILES:
            lend.image = request.FILES['uploadpicture']
        lend.save()
        context_dict = {'ad_slug': lend.slug, 'category': "lendandsell"}
        return ad_posted(request, context_dict)

    else:
        lendAndSell_form = LendAndSellForm()

    return render(request, 'tbc/postlendandsell.html', {'lendAndSell_form': lendAndSell_form})

@login_required
def post_project(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        project = Projects.objects.get_or_create(title=request.POST.get('title'), profile=profile)[0]
        project.description = request.POST.get('description')
        project.lookingFor = request.POST.get('lookingfor')
        project.timeline = request.POST.get('timeline')
        project.keywords = request.POST.get('keywords')
        if 'pictureupload' in request.FILES:
            project.image = request.FILES['pictureupload']
        project.save()
        context_dict = {'ad_slug': project.slug, 'category': "projects"}
        return ad_posted(request, context_dict)

    else:
        project_form = ProjectForm()

    return render(request, 'tbc/postproject.html', {'project_form': project_form})
    
@login_required
def post_service(request):
    if request.method == 'POST':
        desc = request.POST.get('description')
        profile = Profile.objects.get(user=request.user)
        service = Service.objects.get_or_create(title=request.POST.get('title'), profile=profile, description=desc)[0]

        service.price = request.POST.get('price')
        service.keywords = request.POST.get('keywords')
        service.location = request.POST.get('location')
        service.availability = request.POST.get('availability')


        if 'pictureupload' in request.FILES:
            service.image = request.FILES['pictureupload']

        service.save()
        context_dict = {'ad_slug': service.slug, 'category': "services"}
        return ad_posted(request, context_dict)

    else:
        service_form = ServiceForm()
    return render(request, 'tbc/postservice.html', {'service_form': service_form})

@login_required
def post_ad(request):

    lendAndSell_form = LendAndSellForm()
    project_form = ProjectForm()
    service_form = ServiceForm()

    return render(request, 'tbc/postad.html', {'lendAndSell_form': lendAndSell_form, 'project_form': project_form, 'service_form': service_form})


def ad_posted(request, context_dict):
    return render(request, 'tbc/adposted.html', context_dict)


def signup(request):

    registered = False
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.username = user.username
            profile.save()
            login(request, user)

            registered = True
        else:

            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request,'tbc/signup.html', {'user_form': user_form,'profile_form': profile_form,'registered': registered})


@login_required
def editprofile(request):
    edited = False
    currUser = request.user
    # print(currUser.username)
    profile = Profile.objects.get(user=currUser)
    print(profile.skills)

    form = ProfileForm(instance=profile)

    if request.method == 'POST':

        profile.firstname = request.POST.get('firstname')
        profile.lastname = request.POST.get('lastname')
        profile.profession = request.POST.get('profession')
        profile.location = request.POST.get('location')
        profile.skills = request.POST.get('skills')
        profile.education = request.POST.get('education')
        profile.aboutme = request.POST.get('aboutme')
        if 'uploadprofilepicture' in request.FILES:
            profile.image = request.FILES['uploadprofilepicture']
 

        profile.save()
        edited = True

    context_dict = {'form': form, 'profile': profile, 'edited': edited}

    return render(request, 'tbc/editprofile.html', context_dict)

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

def email(request):
    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            #from_email = contact_form.cleaned_data['from_email']
            from_email = ['sender@mail.com']
            #to_email = [form.cleaned_data['to_email']]
            to_email = ['recipient@mail.com']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, to_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('email_sent')
    return render(request, 'tbc/email.html', {'contact_form': contact_form,})

def email_sent(request):
    return HttpResponse('Success! The email was sent.')
