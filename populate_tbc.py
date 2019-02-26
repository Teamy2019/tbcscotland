import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tbc_scotland_project.settings')

import django
django.setup()
from tbc.models import Profile, Inbox, LendAndSell, Service, Projects

def populate():


    John_L_and_S = [
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

    Randy_L_and_S = [
        {"title": "Bass Guitar",
        "description": "Old Bass Guitar",
        "price": "£45",
        "availability": "Til Tuesday",
        "keywords": "Bass, Old"},
        {"title": "Speaker",
        "description": "Biiiiig speaker",
        "price": "£25",
        "availability": "Anytime, anyplace",
        "keywords": "Speaker, Big"} ]
    
    user_profiles = [
        {"name": "Randy",
        "ads": Randy_L_and_S},
        {"name": "John",
        "ads": John_L_and_S} ]

#This isn't right
    for x in user_profiles:
        profile = add_profile(x["name"])
        for l in x["ads"]:
            add_L_and_S(profile, l["title"], l["description"], l["price"], l["availability"], l["keywords"])    
    


def add_L_and_S(profile, title, description, price, availability, keywords):
    l = LendAndSell.objects.get_or_create(title=title, profile=profile)[0]
    l.description=description
    l.price=price
    l.availability=availability
    l.keywords=keywords
    l.save()
    return l

def add_profile(name):
    p = Profile.objects.get_or_create(name=name)[0]
    p.save()
    return p

if __name__ == '__main__':
    print("starting tbc population script...")
    populate()