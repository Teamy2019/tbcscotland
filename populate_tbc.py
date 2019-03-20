import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tbc_scotland_project.settings')

import django
django.setup()
from tbc.models import Profile, LendAndSell, Service, Projects
from django.contrib.auth.models import User

def populate():

    profile_list = [
        {"username" : "encyclopediatax", "firstname": "John", "lastname" : "Smith", "profession": "Art director", "skills" : "Communication", "education" : "Glasgow University", "aboutme" : "It was so terribly cold. Snow was falling, and it was almost dark. Evening came on, the last evening of the year. In the cold and gloom a poor little girl, bareheaded and barefoot, was walking through the streets.", "location" : "Glasgow"},
        {"username" : "guillotinetv", "firstname": "Artemisia", "lastname" : "Gentileschi", "profession": "Painter", "skills" : "French", "education" : "Stirling University", "aboutme" : "Of course when she had left her house she'd had slippers on, but what good had they been? They were very big slippers, way too big for her, for they belonged to her mother.", "location" : "Stirling"},
        {"username" : "balconyrain", "firstname": "Marina", "lastname" : "Abramović", "profession": "Artist", "skills" : "Guitar", "education" : "GSA", "aboutme" : "The little girl had lost them running across the road, where two carriages had rattled by terribly fast. One slipper she'd not been able to find again, and a boy had run off with the other, saying he could use it very well as a cradle some day when he had children of his own.", "location" : "Cordoba"},
        {"username" : "rosesthunder", "firstname": "Jane", "lastname" : "Hawkins", "profession": "Painter", "skills" : "Painting", "education" : "Sorbonne", "aboutme" : "No one had bought any from her all day long, and no one had given her a cent.", "location" : "Berlin"},
        {"username" : "robotbreath", "firstname": "Yeşim", "lastname" : "Ağaoğlu", "profession": "Drummer", "skills" : "Drumming", "education" : "Istanbul University", "aboutme" : "Shivering with cold and hunger, she crept along, a picture of misery, poor little girl! The snowflakes fell on her long fair hair, which hung in pretty curls over her neck. In all the windows lights were shining, and there was a wonderful smell of roast goose, for it was New Year's eve. Yes, she thought of that!", "location" : "Strathbungo"},
        {"username" : "uniformsalon", "firstname": "Justine", "lastname" : "Cooper", "profession": "Painter", "skills" : "Italian", "education" : "Oxford University", "aboutme" : "In a corner formed by two houses, one of which projected farther out into the street than the other, she sat down and drew up her little feet under her. She was getting colder and colder, but did not dare to go home, for she had sold no matches, nor earned a single cent, and her father would surely beat her.", "location" : "Scotstoun"},
        {"username" : "beachseed", "firstname": "Stuart", "lastname" : "Rawlinson", "profession": "Thief", "skills" : "Video Editing", "education" : "Anniesland College", "aboutme" : "Besides, it was cold at home, for they had nothing over them but a roof through which the wind whistled even though the biggest cracks had been stuffed with straw and rags.", "location" : "Yoker"},
        {"username" : "loompromotion", "firstname": "James", "lastname" : "Broun", "profession": "Mage", "skills" : "Sound Production", "education" : "Cardonald College", "aboutme" : "Her hands were almost dead with cold. Oh, how much one little match might warm her! If she could only take one from the box and rub it against the wall and warm her hands. She drew one out. R-r-ratch!", "location" : "Mount Florida"},
        {"username" : "flowerpothail", "firstname": "Rosie", "lastname" : "Watson", "profession": "Photographer", "skills" : "Photography", "education" : "Langside College", "aboutme" : "How it sputtered and burned! It made a warm, bright flame, like a little candle, as she held her hands over it; but it gave a strange light! It really seemed to the little girl as if she were sitting before a great iron stove with shining brass knobs and a brass cover.", "location" : "Paris"},
        {"username" : "tunnelenzyme", "firstname": "Frank", "lastname" : "Underwood", "profession": "Carpenter", "skills" : "Woodwork", "education" : "Goldsmiths", "aboutme" : "How wonderfully the fire burned! How comfortable it was! The youngster stretched out her feet to warm them too; then the little flame went out, the stove vanished, and she had only the remains of the burnt match in her hand.", "location" : "Belfast"},
        # {"username" : "breakfastmidget", "firstname": "Artemisia", "lastname" : "Gentileschi", "profession": "Painter", "skills" : "French", "education" : "Stirling University", "aboutme" : "Of course when she had left her house she'd had slippers on, but what good had they been? They were very big slippers, way too big for her, for they belonged to her mother.", "location" : "Kilmarnock"},
        # {"username" : "filehoney", "firstname": "Artemisia", "lastname" : "Gentileschi", "profession": "Painter", "skills" : "French", "education" : "Stirling University", "aboutme" : "Of course when she had left her house she'd had slippers on, but what good had they been? They were very big slippers, way too big for her, for they belonged to her mother.", "location" : "Inverness"}

    ]

    user_list = [
        {"username" : "encyclopediatax", "password" : "test", "email" : "encyclopediatax@gmail.com"},
        {"username" : "guillotinetv", "password" : "test", "email" : "guillotinetv@gmail.com"},
        {"username" : "balconyrain", "password" : "test", "email" : "balconyrain@gmail.com"},
        {"username" : "rosesthunder", "password" : "test", "email" : "rosesthunder@gmail.com"},
        {"username" : "robotbreath", "password" : "test", "email" : "robotbreath@gmail.com"},
        {"username" : "uniformsalon", "password" : "test", "email" : "uniformsalon@gmail.com"},
        {"username" : "beachseed", "password" : "test", "email" : "beachseed@gmail.com"},
        {"username" : "loompromotion", "password" : "test", "email" : "loompromotion@gmail.com"},
        {"username" : "flowerpothail", "password" : "test", "email" : "flowerpothail@gmail.com"},
        {"username" : "tunnelenzyme", "password" : "test", "email" : "tunnelenzyme@gmail.com"},
        {"username" : "duskscreen", "password" : "test", "email" : "duskscreen@gmail.com"},
        # {"username" : "breakfastmidget", "password" : "test", "email" : "breakfastmidget@gmail.com"},
        # {"username" : "filehoney", "password" : "test", "email" : "filehoney@gmail.com"}
    ]

    sample_L_and_S = [
        {"username" : "encyclopediatax", "title": "Guitar", "description": "7 stringed guitar for sale.", "price": "£75", "availability": "Now", "keywords" : "guitar, 7, strings, sale"},
        {"username" : "guillotinetv", "title": "Effects Pedal", "description": "Cool effects pedal to borrow.", "price": "£0", "availability": "Weekends", "keywords" : "weekends, pedal, effects pedal, guitar, lend"}
    ]


    sample_services = [
        {"username" : "encyclopediatax", "title": "Piano lessons", "description": "Fun and helpful piano tutor", "price": "£10 per hour", "availability": "Evenings only, once or twice per week", "keywords": "Piano, tutoring, weekly", "location": "Glasgow" },
        {"username" : "guillotinetv", "title": "Sound technician services", "description": "Experienced freelance technician looking for projects", "price": "Negotiable", "availability": "Evenings and weekends only", "keywords": "Technician, experienced, freelance", "location": "Aberdeen"},
        {"username" : "duskscreen", "title": "Camera work", "description": "Experienced freelance cameraperson looking to help YOU make a movie!", "price": "Negotiable", "availability": "Evenings only", "keywords": "cool, cameraperson, strong, experienced, freelance", "location": "Montrose"},
        {"username" : "tunnelenzyme", "title": "Stuntperson", "description": "Amazing stunts NO TIMEWASTERS. CALL NOW FOR a freelance stuntperson looking cool action movie projects", "price": "£100 per hour", "availability": "Anytime", "keywords": "stunt, stunts, cool, movies, experienced, freelance", "location": "Townhead"},
        {"username" : "uniformsalon", "title": "Kiln for hire", "description": "Make pottery with me and my kiln!", "price": "£1 a pot", "availability": "Anytime", "keywords": "potter, pottery, freelance", "location": "Moffat"}

    ]
    
    sample_projects = [
        {"username" : "encyclopediatax", "title": "Sound art festival", "description": "A new and exciting sound art festival looking for participants", "lookingfor": "Artists and experimental musicians", "timeline": "Accepting proposals throughout May", "keywords": "Sound art, festival"},
        {"username" : "guillotinetv", "title": "Short film - drama", "description": "Recent RCS graduate looking for volunteers to help complete a short film", "lookingfor": "Looking for actors and editors", "timeline": "Looking to finish cast before commencing principle shoots next month, editing timeline a bit more flexible", "keywords": "Film, actors, editors"}
    ]


    for u in user_list:
        user = add_user(u['username'], u['password'], u['email'])
        for p in profile_list:
            if user.username == p['username']: 
                profile = add_profile(user, p["username"], p["firstname"], p["lastname"], p["profession"], p["skills"], p["education"], p["aboutme"], p["location"])
                for l in sample_L_and_S:
                    if user.username == l['username']:
                        add_L_and_S(profile, l['title'], l['description'], l['price'], l['availability'], l['keywords'])

                for s in sample_services:
                    if user.username == s['username']:
                        add_services(profile, s['title'], s['description'], s['price'], s['availability'], s['keywords'], s['location'])

                for pr in sample_projects:
                    if user.username == pr['username']:
                        add_project(profile, pr['title'], pr['description'], pr['lookingfor'], pr['timeline'], pr['keywords'])


        # for p in profile_list:
        #    add_profile(user, p["username"], p["firstname"], p["lastname"], p["profession"], p["skills"], p["education"], p["aboutme"], p["location"])

        # for profiles in profile_list:
        #     profile = add_profile(user, profile_list["firstname"], profile_list["lastname"], profile_list["profession"], profile_list["skills"], profile_list["education"], profile_list["aboutme"], profile_list["location"])
        # for lends in sample_L_and_S:
        #     add_L_and_S(profile, lends["title"], lends["description"], lends["price"], lends["availability"], lends["keywords"])
        # for service in sample_services:
        #     add_services(profile, service["title"], service["description"], service["price"], service["availability"], service["keywords"], service["location"])
        # for projects in sample_projects:
        #     add_project(profile, projects["title"], projects["description"], projects["lookingfor"], projects["timeline"], projects["keywords"])
        
def add_L_and_S(profile, title, description, price, availability, keywords):
    l = LendAndSell.objects.get_or_create(
                                    title=title,
                                    profile=profile)[0]
    l.title=title
    l.description=description
    l.price=price
    l.availability=availability
    l.keywords=keywords
    l.save()
    return l

def add_services(profile, title, description, price, availability, keywords, location):
    s = Service.objects.get_or_create(  
                                    title=title,
                                    profile=profile)[0]
    s.title=title
    s.description=description
    s.price=price
    s.availability=availability
    s.keywords=keywords
    s.location=location
    s.save()
    return s

def add_project(profile, title, description, lookingfor, timeline, keywords):
    p = Projects.objects.get_or_create(
                                    title=title,
                                    profile=profile
                                    )[0]
    p.title=title
    p.description=description
    p.lookingfor=lookingfor
    p.timeline=timeline
    p.keywords=keywords
    p.save()
    return p

def add_profile(user, username, firstname, lastname, profession, skills, education, aboutme, location):
    p = Profile.objects.get_or_create(
                                    user=user,
                                    username=username,
                                    firstname=firstname,
                                    lastname=lastname,
                                    profession=profession,
                                    skills=skills,
                                    education=education,
                                    aboutme=aboutme,
                                    location=location
                                    )[0]
    p.save()
    return p

def add_user(username, password, email):
    u = User.objects.get_or_create(
                                    username=username,
                                    password=password,
                                    email=email
                                    )[0]
    u.save()
    return u

if __name__ == '__main__':
    print("starting tbc population script...")
    populate()
