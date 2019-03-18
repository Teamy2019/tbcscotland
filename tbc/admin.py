from django.contrib import admin
from tbc.models import Profile, Inbox, LendAndSell, Service, Projects, UserProfile, Comments

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'aboutme')

class LendAndSellAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile', 'description')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('profile', 'author')

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Inbox)
admin.site.register(LendAndSell)
admin.site.register(Service)
admin.site.register(Projects)
admin.site.register(UserProfile)
admin.site.register(Comments)
