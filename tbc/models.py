from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

#Should this be from a pre-determined list? Like the shirt sizes
# here: https://docs.djangoproject.com/en/2.1/topics/db/models/
class Category(models.Model):
    name = models.CharField(max_length=128)
    views = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='profile_images', blank=True)
    skills = models.TextField()
    education = models.TextField()
    aboutme = models.TextField()
    slug = models.SlugField(unique=True)
    portfolio = models.ImageField(upload_to='portfolio_images', blank=True)
    activities = models.ImageField(upload_to='activities_images', blank=True)
    views = models.IntegerField(default=0)
    reviews = models.TextField()
    # location
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=128)
    username = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Ad(models.Model):
    category = models.ForeignKey(Category)
    profile = models.ForeignKey(Profile)
    title = models.CharField(max_length=128)
    # startdate
    # enddate
    description = models.TextField()
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='ad_images', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Ad, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Inbox(models.Model):
    ad = models.ForeignKey(Ad)
    messages = models.TextField()
    sender = models.ForeignKey(Profile)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Inbox, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


