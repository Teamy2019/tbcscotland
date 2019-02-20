from django.conf.urls import url
from tbc import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^about/', views.about, name='about'),
    url(r'^getstarted/', views.getstarted, name='getstarted'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^profiles/', views.profiles, name='profiles'),
    url(r'^lendandsell/', views.lendandsell, name='lendandsell'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^services/', views.services, name='services'),
]