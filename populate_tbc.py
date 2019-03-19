import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tbc_scotland_project.settings')

import django
django.setup()
from tbc.models import Profile, Inbox, LendAndSell, Service, Projects

def populate():

    profile_list = [
        {"name": "John Smith"} ]


    sample_L_and_S = [
        {"title": "Guitar",
        "description": "Lovely guitar",
        "price": "£75",
        "availability": "Until Sold",
        "keywords": "Guitar, Lovely"},
        {"title": "Effects Pedal",
        "description": "Cool effects pedal",
        "price": "£30",
        "availability": "Until Wednesday",
        "keywords": "Cool, Effects"} ]

    sample_services = [
        {"title": "Piano lessons",
        "description": "Fun and helpful piano tutor",
        "price": "£10 per hour",
        "availability": "Evenings only, once or twice per week",
        "keywords": "Piano, tutoring, weekly",
        "location": "Glasgow" },
        {"title": "Sound technician",
        "description": "Experienced freelance technician looking for projects",
        "price": "Negotiable",
        "availability": "Evenings and weekends only",
        "keywords": "Technician, experienced, freelance",
        "location": "Edinburgh"} ]
    
    sample_projects = [
        {"title": "Sound art festival",
        "description": "A new and exciting sound art festival looking for participants",
        "lookingFor": "Artists and experimental musicians",
        "timeline": "Accepting proposals throughout May",
        "keywords": "Sound art, festival"},
        {"title": "Short film - drama",
        "description": "Recent RCS graduate looking for volunteers to help complete a short film",
        "lookingFor": "Looking for actors and editors",
        "timeline": "Looking to finish cast before commencing principle shoots next month, editing timeline a bit more flexible",
        "keywords": "Film, actors, editors"} ]

    for profiles in profile_list:
        profile = add_profile(profiles["name"])
       
        for lends in sample_L_and_S:
            add_L_and_S(profile, lends["title"], lends["description"], lends["price"], lends["availability"], lends["keywords"])
        for service in sample_services:
            add_services(profile, service["title"], service["description"], service["price"], service["availability"], service["keywords"], service["location"])
        for projects in sample_projects:
            add_project(profile, projects["title"], projects["description"], projects["lookingFor"], projects["timeline"], projects["keywords"])
        
# #This isn't right
#     for x in user_profiles:
#         profile = add_profile(x["name"])
#         # for l in x["ads"]:
#         #     add_L_and_S(profile, l["title"], l["description"], l["price"], l["availability"], l["keywords"])   


    


def add_L_and_S(profile, title, description, price, availability, keywords):
    l = LendAndSell.objects.get_or_create(title=title, profile=profile)[0]
    l.description=description
    l.price=price
    l.availability=availability
    l.keywords=keywords
    l.save()
    return l

def add_services(profile, title, description, price, availability, keywords, location):
    s = Service.objects.get_or_create(title=title, profile=profile)[0]
    s.description=description
    s.price=price
    s.availability=availability
    s.keywords=keywords
    s.location
    s.save()
    return s

def add_project(profile, title, description, lookingFor, timeline, keywords):
    p = Projects.objects.get_or_create(title=title, profile=profile)[0]
    p.description=description
    p.lookingFor=lookingFor
    p.timeline=timeline
    p.keywords=keywords
    p.save()
    return p    

def add_profile(name):
    p = Profile.objects.get_or_create(name=name)[0]
    p.save()
    return p

if __name__ == '__main__':
    print("starting tbc population script...")
    populate()