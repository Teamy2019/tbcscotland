from django import forms
from django.contrib.auth.models import User
from tbc.models import UserProfile
from tbc.models import LendAndSell, Projects, Service

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class LendAndSellForm(forms.ModelForm):
    #profile = forms.CharField(widget=forms.HiddenInput(), required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    image = forms.ImageField(required=False)
    title = forms.CharField(help_text="Please enter the title of your ad")
    description = forms.CharField(widget=forms.Textarea, help_text="Tell everyone what it is you're offering")
    keywords = forms.CharField(required=False)


    class Meta:
        model = LendAndSell

        fields = ('title', 'description', 'image', 'price', 'availability', 'keywords')

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

    class Meta:
        model = Projects
        fields = ('title', 'image', 'description', 'lookingFor', 'timeline', 'keywords')

class ServiceForm(forms.ModelForm):
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    image = forms.ImageField(required=False)
    title = forms.CharField(help_text="Please enter the title of your ad")
    description = forms.CharField(widget=forms.Textarea, help_text="Tell everyone about the pService you can provide")
    price = forms.CharField(max_length=128, required=False)
    availability = forms.CharField(max_length=256, required=False)
    keywords = forms.CharField(required=False)
    location = forms.CharField(required=False)

    class Meta:
        model = Service
        fields = ('title', 'image', 'description', 'price', 'availability', 'keywords', 'location')





