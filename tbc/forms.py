from django import forms
from django.contrib.auth.models import User
from tbc.models import UserProfile, Profile
from tbc.models import LendAndSell, Projects, Service
from django.db.models import Q
import operator

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    firstname = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    is_company = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'firstname', 'surname', 'email', 'password', 'is_company')

# class ProfileForm(forms.ModelForm):
#     image = forms.ImageField(required=False)
#     skills = forms.TextField(required=False)
#     education = forms.TextField(required=False)
#     slug = forms.CharField(widget=forms.HiddenInput(), required=False)
#     aboutme = forms.TextField(required=False)
#     portfolio = forms.ImageField(required=False)
#     activities = forms.ImageField(required=False)

#     class Meta:
#         model = Profile
#         field = ('image', 'skills', 'education', 'aboutme', 'portfolio', 'activities')

#class UserProfileForm(forms.ModelForm):
#    class Meta:
#        model = UserProfile
#        fields = ('website', 'picture')

class UserProfileForm(forms.ModelForm):
    aboutme = forms.CharField(widget=forms.Textarea, required=False)
    skills = forms.CharField(widget=forms.Textarea, required=False)
    education = forms.CharField(widget=forms.Textarea, required=False)
    picture = forms.ImageField(required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    name = forms.CharField(widget=forms.HiddenInput(), required=False)



    class Meta:
        model = UserProfile
        fields = ('aboutme', 'skills', 'education', 'picture')

class LendAndSellForm(forms.ModelForm):
    #profile = forms.CharField(widget=forms.HiddenInput(), required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    image = forms.ImageField(required=False)
    title = forms.CharField(help_text="Please enter the title of your ad")
    description = forms.CharField(widget=forms.Textarea, help_text="Tell everyone what it is you're offering")
    keywords = forms.CharField(required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = LendAndSell

        fields = ('title', 'description', 'image', 'price', 'availability', 'keywords', 'profile')

class ProjectForm(forms.ModelForm):
  # profile should link atuomatically!!!  profile = forms.CharField(widget=forms.HiddenInput(), required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    image = forms.ImageField(required=False)
    title = forms.CharField(help_text="Please enter the title of your ad")
    description = forms.CharField(widget=forms.Textarea, help_text="Tell everyone about the project you're working on")
    lookingFor = forms.CharField(widget=forms.Textarea, help_text="What do you need?")
    timeline = forms.CharField(widget=forms.Textarea, help_text="When do you need it? How long for?")
    keywords = forms.CharField(required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Projects
        fields = ('title', 'image', 'description', 'lookingFor', 'timeline', 'keywords', 'profile')

class ServiceForm(forms.ModelForm):
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    image = forms.ImageField(required=False)
    title = forms.CharField(help_text="Please enter the title of your ad")
    description = forms.CharField(widget=forms.Textarea, help_text="Tell everyone about the Service you can provide")
    price = forms.CharField(max_length=128, required=False)
    availability = forms.CharField(max_length=256, required=False)
    keywords = forms.CharField(required=False)
    location = forms.CharField(required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Service
        fields = ('title', 'image', 'description', 'price', 'availability', 'keywords', 'location', 'profile')

# class Search(Search):
#     paginate_by = 10
#     def get_queryset(self):
#         result = super(Search, self).get_queryset()

#         query = self.request.GET.get('q')
#         if query:
#             query_list = query.split()
#             result = result.filter(
#                 reduce(operator.and_,
#                     (Q(LendAndSell__icontains=q) for q in query_list)) |
#                 reduce(operator.and_,
#                     (Q(LendAndSell__icontains=q) for q in query_list))
#             )
#         return result
