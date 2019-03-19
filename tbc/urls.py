from django.conf.urls import url
from tbc import views
from tbc.views import search

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^about/', views.about, name='about'),
    url(r'^getstarted/', views.getstarted, name='getstarted'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^editprofile/$', views.editprofile, name='editprofile'),
    url(r'^profiles/$', views.profiles, name='profiles'),
    url(r'^lendandsell/$', views.lendandsell, name='lendandsell'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^services/$', views.services, name='services'),
    url(r'^lendandsell/(?P<lendandsell_name_slug>[\w\-]+)/$', views.show_lendandsell, name='show_lendandsell'),
    url(r'^projects/(?P<project_name_slug>[\w\-]+)/$', views.show_project, name='show_project'),
    url(r'^services/(?P<service_name_slug>[\w\-]+)/$', views.show_service, name='show_service'),
    url(r'^profiles/(?P<profile_name_slug>[\w\-]+)/$', views.show_profile, name='show_profile'),
    url(r'^postad/$', views.post_ad, name='post_ad'),
    url(r'^postlendandsell/$', views.post_lendAndSell, name='post_lendandsell'),
    url(r'^postproject/$', views.post_project, name='post_project'),
    url(r'^postservice/$', views.post_service, name='post_service'),
    url(r'^adposted/$', views.ad_posted, name='ad_posted'),
    url(r'^email/$', views.email, name='email'),
    url(r'success/$', views.email_sent, name='email_sent'),
]
