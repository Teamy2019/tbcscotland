from django.contrib import admin
from tbc.models import Profile, Inbox, LendAndSell, Service, Projects


# Register your models here.
admin.site.register(Profile)
admin.site.register(Inbox)
admin.site.register(LendAndSell)

admin.site.register(Service)

admin.site.register(Projects)

