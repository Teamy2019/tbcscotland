from django import forms
from django.contrib.auth.models import User
from tbc.models import Profile
from tbc.models import LendAndSell, Projects, Service, Comments
from django.db.models import Q
import operator

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class ProfileForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.HiddenInput(), required=False)
    lastname = forms.CharField(widget=forms.HiddenInput(), required=False)
    profession = forms.CharField(widget=forms.HiddenInput(), required=False)
    image = forms.ImageField(required=False)
    skills = forms.CharField(widget=forms.HiddenInput(), required=False)
    education = forms.CharField(widget=forms.HiddenInput(), required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    aboutme = forms.CharField(widget=forms.HiddenInput(), required=False)
    location = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Profile
        fields = ('image',)


class LendAndSellForm(forms.ModelForm):
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    image = forms.ImageField(required=False)
    title = forms.CharField(help_text="Please enter the title of your ad")
    description = forms.CharField(widget=forms.Textarea, help_text="Tell everyone what it is you're offering")
    keywords = forms.CharField(required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = LendAndSell

        fields = ('title', 'description', 'image', 'price', 'availability', 'keywords')

class ProjectForm(forms.ModelForm):
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
        fields = ('title', 'image', 'description', 'lookingFor', 'timeline', 'keywords')

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
        fields = ('title', 'image', 'description', 'price', 'availability', 'keywords', 'location')

class CommentsForm(forms.ModelForm):
    comment = forms.CharField(max_length=256, required=True)
    # date_created = forms.DateField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Comments
        fields = ('comment',)

class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

#    class Meta:
#        model = Contact
#        fields = ('subject', 'message')
