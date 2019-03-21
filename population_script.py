import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tbc_scotland_project.settings')

import django
django.setup()
from tbc.models import Profile, LendAndSell, Service, Projects
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from django.conf.urls.static import static


def populate():

    profile_list = [
       # {"username" : "encyclopediatax", "firstname": "John", "lastname" : "Smith", "profession": "Art director", "skills" : "Communication", "education" : "Glasgow University", "aboutme" : "It was so terribly cold. Snow was falling, and it was almost dark. Evening came on, the last evening of the year. In the cold and gloom a poor little girl, bareheaded and barefoot, was walking through the streets.", "location" : "Glasgow", "image" : finders.find("s1.jpg")},
       # {"username" : "guillotinetv", "firstname": "Artemisia", "lastname" : "Gentileschi", "profession": "Painter", "skills" : "French", "education" : "Stirling University", "aboutme" : "Of course when she had left her house she'd had slippers on, but what good had they been? They were very big slippers, way too big for her, for they belonged to her mother.", "location" : "Stirling", "image" : finders.find("s2.jpg")},
       # {"username" : "balconyrain", "firstname": "Marina", "lastname" : "Abramović", "profession": "Artist", "skills" : "Guitar", "education" : "GSA", "aboutme" : "The little girl had lost them running across the road, where two carriages had rattled by terribly fast. One slipper she'd not been able to find again, and a boy had run off with the other, saying he could use it very well as a cradle some day when he had children of his own.", "location" : "Cordoba", "image" : finders.find("s3.jpg")},
       # {"username" : "rosesthunder", "firstname": "Jane", "lastname" : "Hawkins", "profession": "Painter", "skills" : "Painting", "education" : "Sorbonne", "aboutme" : "No one had bought any from her all day long, and no one had given her a cent.", "location" : "Berlin", "image" : finders.find("s4.jpg")},
       # {"username" : "robotbreath", "firstname": "Yeşim", "lastname" : "Ağaoğlu", "profession": "Drummer", "skills" : "Drumming", "education" : "Istanbul University", "aboutme" : "Shivering with cold and hunger, she crept along, a picture of misery, poor little girl! The snowflakes fell on her long fair hair, which hung in pretty curls over her neck. In all the windows lights were shining, and there was a wonderful smell of roast goose, for it was New Year's eve. Yes, she thought of that!", "location" : "Strathbungo", "image" : finders.find("s5.jpg")},
       # {"username" : "uniformsalon", "firstname": "Justine", "lastname" : "Cooper", "profession": "Painter", "skills" : "Italian", "education" : "Oxford University", "aboutme" : "In a corner formed by two houses, one of which projected farther out into the street than the other, she sat down and drew up her little feet under her. She was getting colder and colder, but did not dare to go home, for she had sold no matches, nor earned a single cent, and her father would surely beat her.", "location" : "Scotstoun", "image" : finders.find("s6.jpg")},
       # {"username" : "beachseed", "firstname": "Stuart", "lastname" : "Rawlinson", "profession": "Thief", "skills" : "Video Editing", "education" : "Anniesland College", "aboutme" : "Besides, it was cold at home, for they had nothing over them but a roof through which the wind whistled even though the biggest cracks had been stuffed with straw and rags.", "location" : "Yoker", "image" : finders.find("s7.jpg")},
       # {"username" : "loompromotion", "firstname": "James", "lastname" : "Broun", "profession": "Mage", "skills" : "Sound Production", "education" : "Cardonald College", "aboutme" : "Her hands were almost dead with cold. Oh, how much one little match might warm her! If she could only take one from the box and rub it against the wall and warm her hands. She drew one out. R-r-ratch!", "location" : "Mount Florida", "image" : finders.find("s8.jpg")},
       # {"username" : "flowerpothail", "firstname": "Rosie", "lastname" : "Watson", "profession": "Photographer", "skills" : "Photography", "education" : "Langside College", "aboutme" : "How it sputtered and burned! It made a warm, bright flame, like a little candle, as she held her hands over it; but it gave a strange light! It really seemed to the little girl as if she were sitting before a great iron stove with shining brass knobs and a brass cover.", "location" : "Paris", "image" : finders.find("s9.jpg")},
       # {"username" : "tunnelenzyme", "firstname": "Frank", "lastname" : "Underwood", "profession": "Carpenter", "skills" : "Woodwork", "education" : "Goldsmiths", "aboutme" : "How wonderfully the fire burned! How comfortable it was! The youngster stretched out her feet to warm them too; then the little flame went out, the stove vanished, and she had only the remains of the burnt match in her hand.", "location" : "Belfast", "image" : finders.find("s10.jpg")},
       # {"username": "duskscreen", "firstname": "Clarice", "lastname": "Starling", "profession": "FBI Agent", "skills": "Catching bad guys", "education": "FBI Academy", "aboutme": "Joined the FBI to avoid my problems at home", "location": "Glasgow", "image" : finders.find("s11.jpg")},
        {"username" : "encyclopediatax", "firstname": "John", "lastname" : "Smith", "profession": "Art director", "skills" : "Communication", "education" : "Glasgow University", "aboutme" : "It was so terribly cold. Snow was falling, and it was almost dark. Evening came on, the last evening of the year. In the cold and gloom a poor little girl, bareheaded and barefoot, was walking through the streets.", "location" : "Glasgow", "image" : "s1.jpg"},
        {"username" : "guillotinetv", "firstname": "Artemis", "lastname" : "Gentil", "profession": "Sound Arist", "skills" : "French", "education" : "Stirling University", "aboutme" : "My name is Artemis Gentil. I am a sound artist hailing from Lanark, Scotland. I contian many sounds often I place them into the air, for others to experience. I contain multitudes and I have much technical experience in editing sound files etc.", "location" : "Glasgow", "image" : "s2.jpg"},
        {"username" : "balconyrain", "firstname": "Marina", "lastname" : "Abramović", "profession": "Artist", "skills" : "Guitar", "education" : "GSA", "aboutme" : "The little girl had lost them running across the road, where two carriages had rattled by terribly fast. One slipper she'd not been able to find again, and a boy had run off with the other, saying he could use it very well as a cradle some day when he had children of his own.", "location" : "Cordoba", "image" : "s3.jpg"},
        {"username" : "rosesthunder", "firstname": "Jane", "lastname" : "Hawkins", "profession": "Painter", "skills" : "Painting", "education" : "Sorbonne", "aboutme" : "No one had bought any from her all day long, and no one had given her a cent.", "location" : "Berlin", "image" : "s4.jpg"},
        {"username" : "robotbreath", "firstname": "Yeşim", "lastname" : "Ağaoğlu", "profession": "Drummer", "skills" : "Drumming", "education" : "Istanbul University", "aboutme" : "Shivering with cold and hunger, she crept along, a picture of misery, poor little girl! The snowflakes fell on her long fair hair, which hung in pretty curls over her neck. In all the windows lights were shining, and there was a wonderful smell of roast goose, for it was New Year's eve. Yes, she thought of that!", "location" : "Strathbungo", "image" : "s5.jpg"},
        {"username" : "uniformsalon", "firstname": "Justine", "lastname" : "Cooper", "profession": "Painter", "skills" : "Italian", "education" : "Oxford University", "aboutme" : "In a corner formed by two houses, one of which projected farther out into the street than the other, she sat down and drew up her little feet under her. She was getting colder and colder, but did not dare to go home, for she had sold no matches, nor earned a single cent, and her father would surely beat her.", "location" : "Scotstoun", "image" : "s6.jpg"},
        {"username" : "beachseed", "firstname": "Stuart", "lastname" : "Rawlinson", "profession": "Thief", "skills" : "Video Editing", "education" : "Anniesland College", "aboutme" : "Besides, it was cold at home, for they had nothing over them but a roof through which the wind whistled even though the biggest cracks had been stuffed with straw and rags.", "location" : "Yoker", "image" : "s7.png"},
        {"username" : "loompromotion", "firstname": "James", "lastname" : "Broun", "profession": "Mage", "skills" : "Sound Production", "education" : "Cardonald College", "aboutme" : "Her hands were almost dead with cold. Oh, how much one little match might warm her! If she could only take one from the box and rub it against the wall and warm her hands. She drew one out. R-r-ratch!", "location" : "Mount Florida", "image" : "s8.jpg"},
        {"username" : "flowerpothail", "firstname": "Rosie", "lastname" : "Watson", "profession": "Photographer", "skills" : "Photography", "education" : "Langside College", "aboutme" : "How it sputtered and burned! It made a warm, bright flame, like a little candle, as she held her hands over it; but it gave a strange light! It really seemed to the little girl as if she were sitting before a great iron stove with shining brass knobs and a brass cover.", "location" : "Paris", "image" : "s9.jpg"},
        {"username" : "tunnelenzyme", "firstname": "Frank", "lastname" : "Underwood", "profession": "Carpenter", "skills" : "Woodwork", "education" : "Goldsmiths", "aboutme" : "How wonderfully the fire burned! How comfortable it was! The youngster stretched out her feet to warm them too; then the little flame went out, the stove vanished, and she had only the remains of the burnt match in her hand.", "location" : "Belfast", "image" : "s10.jpg"},
        {"username": "duskscreen", "firstname": "Clarice", "lastname": "Starling", "profession": "FBI Agent", "skills": "Catching bad guys", "education": "FBI Academy", "aboutme": "Joined the FBI to avoid my problems at home", "location": "Glasgow", "image" : "s11.jpg"},
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
        {"username" : "encyclopediatax", "title": "Guitar", "description": "7 stringed guitar for sale.", "price": "£75", "availability": "Now", "keywords" : "guitar, 7, strings, sale", "image" : "l1.jpg"},
        {"username" : "guillotinetv", "title": "Effects Pedal", "description": "Cool effects pedal to borrow.", "price": "£0", "availability": "Weekends", "keywords" : "weekends, pedal, effects pedal, guitar, lend", "image" : "l2.jpg"},
        {"username" : "duskscreen", "title": "In Search of Lost Books?", "description": "I'm moving house and don't have anywhere to put my full collection of Proust's 'In Search of Lost Time', would anyone like to take it of my hands? It's a really great book.", "price": "Negotiable", "availability": "Before Tuesday 3rd March", "keywords": "Proust books giveaway", "image" : "l3.jpg"},
        {"username" : "uniformsalon", "title": "Amp", "description": "I have an amp that I rarely use anymore, would anyone like to borrow it? I'm only really using it for band practice twice a week and at the occasional gig, so it's available for short loans quite often.", "price": "free to hire", "availability": "Short loans only", "keywords": "Amp Free Short Loans", "image" : "l4.jpg"},
        {"username" : "uniformsalon", "title": "Spare Paint Suppies", "description": "I'm moving house and need to offload some painting supplies I've gathered over the years! I've got brushes, canvas, and thinner. Get in touch if you'd like to know more!", "price": "Depends on item", "availability": "Until May", "keywords": "paint supplies", "image" : "l5.jpeg"},
        {"username" : "beachseed", "title": "Father Time", "description": "Selling my painting 'Father Time', part of my series 'The Fathers Of Us All'.", "price": "£200 or next best offer", "availability": "Available now", "keywords": "Painting Father Time", "image" : "l6.jpg"},
        {"username" : "flowerpothail", "title": "Marrow", "description": "My sculpture 'Marrow' is now for sale after working on it for ten years. It features actual bone marrow, don't ask how I got it!", "price": "£10000", "availability": "Now until forever", "keywords": "Scultpure metal rods Marrow marrow art", "image" : "l7.jpg"},
        {"username" : "robotbreath", "title": "Space Between Plates", "description": "Here is an example of my work, the sculpture 'Space Between Plates'. This piece is for sale. Please contact me if you'd like ot purchase, or view my other work.", "price": "£350", "availability": "Now", "keywords": "sculpture spaces plates", "image" : "l8.jpg"},
    ]


    sample_services = [
        {"username" : "encyclopediatax", "title": "Piano lessons", "description": "Fun and helpful piano tutor", "price": "£10 per hour", "availability": "Evenings only, once or twice per week", "keywords": "Piano, tutoring, weekly", "location": "Glasgow", "image" : "ss1.jpeg"},
        {"username" : "guillotinetv", "title": "Sound technician services", "description": "Experienced freelance technician looking for projects", "price": "Negotiable", "availability": "Evenings and weekends only", "keywords": "Technician, experienced, freelance", "location": "Aberdeen", "image" : "ss2.jpg"},
        {"username" : "duskscreen", "title": "Camera work", "description": "Experienced freelance cameraperson looking to help YOU make a movie!", "price": "Negotiable", "availability": "Evenings only", "keywords": "cool, cameraperson, strong, experienced, freelance", "location": "Montrose", "image" : "ss3.jpg"},
        {"username" : "tunnelenzyme", "title": "Stuntperson", "description": "Amazing stunts NO TIMEWASTERS. CALL NOW FOR a freelance stuntperson looking cool action movie projects", "price": "£100 per hour", "availability": "Anytime", "keywords": "stunt, stunts, cool, movies, experienced, freelance", "location": "Townhead", "image" : "ss4.jpg"},
        {"username" : "uniformsalon", "title": "Kiln for hire", "description": "Make pottery with me and my kiln!", "price": "£1 a pot", "availability": "Anytime", "keywords": "potter, pottery, freelance", "location": "Moffat", "image" : "ss5.jpeg"},
        {"username" : "rosesthunder", "title": "Editor", "description": "Experinced manuscript editor seeking clients. I am very flexible with timelines and have managed lots of projects before. I edited Paradise Lost. Contact me to find out how it ends.", "price": "Negotiable", "availability": "Part time hours only", "keywords": "Editor writing", "location": "Edinburgh", "image" : "ss6.gif"},
        {"username" : "loompromotion", "title": "Set Designer", "description": "I have designed many sets in my time and I would love nothing more than to design yours. I live to design sets.", "availability": "All the time", "price": "Whatever you can afford", "keywords": "Set Design", "location": "Partick", "image" : "ss7.jpeg"},
        {"username" : "balconyrain", "title": "Muse", "description": "I have seven years experence as an artist's muse, currently seeking a new opportunity. I can provide a sultry escape from your life and the promise of something better yet ultimately deliciously unattainable. Find out more today!", "availability": "When I choose", "price": "Your soul, your talent, your marraige.", "keywords": "What are you waiting for?", "location": "Just out of reach.", "image" : "ss8.jpg"},
    ]
    
    sample_projects = [
        {"username" : "encyclopediatax", "title": "Sound art festival", "description": "A new and exciting sound art festival looking for participants", "lookingfor": "Artists and experimental musicians", "timeline": "Accepting proposals throughout May", "keywords": "Sound art, festival", "image" : "p1.jpg"},
        {"username" : "guillotinetv", "title": "Short film - drama", "description": "Recent RCS graduate looking for volunteers to help complete a short film", "lookingfor": "Looking for actors and editors", "timeline": "Looking to finish cast before commencing principle shoots next month, editing timeline a bit more flexible", "keywords": "Film, actors, editors", "image" : "p2.jpeg"},
        {"username" : "duskscreen", "title": "City-wide festival", "description": "Glasgow-based music festival. YOu probably haven't heard of us, but we've been going for years. We only put on cool tunes, don't make requests. We will change your fucking life.", "lookingfor": "punters and musicians", "timeline": "We will surprise you", "keywords": "cool sound festival", "image" : "p3.jpg"},
        {"username" : "duskscreen", "title": "Experimental Theatre Production", "description": "I lost a bet and now I have to put on a play next week. I though it would be funnier to make it crazy and weird, anyone into that?", "lookingfor": "Fellow collaborators - HAHAHA", "timeline": "Soon!!!", "keywords": "theatre experimental play", "image" : "p4.jpg"},
        {"username" : "loompromotion", "title": "Twelfth Night", "description": "AmDram production of The Bard's Best Play (I'll fight anyone who says otherwise!) We're looking for Malvolio, have you seen him?", "lookingfor": "Actor capable of conveying Malvolio's characteristics", "timeline": "Sometime this week would be preferable!", "keywords": "art culture Shakespeare Twelfth Night Malvolio", "image" : "p5.jpg"},
        {"username" : "duskscreen", "title": "Guiness World Record Attempt", "description": "Looking for people to take part in a human pyramid", "lookingfor": "Anyone <90kg", "timeline": "Accepting proposals throughout May", "keywords": "guinness, world, record, human, pyramid", "image" : "p6.jpg"},
        {"username" : "flowerpothail", "title": "SHOOTING A MOVIE", "description": "My wife and I need a cameraperson for our movie project", "lookingfor": "Experienced cameraperson, over 3 years experience", "timeline": "This weekend", "keywords": "movie, film, art", "image" : "p7.jpg"},
        {"username" : "robotbreath", "title": "BAKE OFF", "description": "Come and see if you can beat me in a BAKE OFF", "lookingfor": "Real bakers.", "timeline": "May", "keywords": "bake, off, bake off, cakes", "image" : "p8.jpg"}
    ]



    for u in user_list:
        user = add_user(u['username'], u['password'], u['email'])
        for p in profile_list:
            if user.username == p['username']: 
                profile = add_profile(user, p["username"], p["firstname"], p["lastname"], p["profession"], p["skills"], p["education"], p["aboutme"], p["location"], p["image"])
                for l in sample_L_and_S:
                    if user.username == l['username']:
                        add_L_and_S(profile, l['title'], l['description'], l['price'], l['availability'], l['keywords'], l["image"])

                for s in sample_services:
                    if user.username == s['username']:
                        add_services(profile, s['title'], s['description'], s['price'], s['availability'], s['keywords'], s['location'], s["image"])

                for pr in sample_projects:
                    if user.username == pr['username']:
                        add_project(profile, pr['title'], pr['description'], pr['lookingfor'], pr['timeline'], pr['keywords'], pr["image"])


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
        
def add_L_and_S(profile, title, description, price, availability, keywords, image):
    l = LendAndSell.objects.get_or_create(
                                    title=title,
                                    profile=profile)[0]
    l.title=title
    l.description=description
    l.price=price
    l.availability=availability
    l.keywords=keywords
    l.image=image
    l.save()
    return l

def add_services(profile, title, description, price, availability, keywords, location, image):
    s = Service.objects.get_or_create(  
                                    title=title,
                                    profile=profile)[0]
    s.title=title
    s.description=description
    s.price=price
    s.availability=availability
    s.keywords=keywords
    s.location=location
    s.image=image
    s.save()
    return s

def add_project(profile, title, description, lookingfor, timeline, keywords, image):
    p = Projects.objects.get_or_create(
                                    title=title,
                                    profile=profile
                                    )[0]
    p.title=title
    p.description=description
    p.lookingfor=lookingfor
    p.timeline=timeline
    p.keywords=keywords
    p.image=image
    p.save()
    return p

def add_profile(user, username, firstname, lastname, profession, skills, education, aboutme, location, image):
    #picture = image
    #i = finders.find(image)
    p = Profile.objects.get_or_create(
                                    user=user,
                                    username=username,
                                    firstname=firstname,
                                    lastname=lastname,
                                    profession=profession,
                                    skills=skills,
                                    education=education,
                                    aboutme=aboutme,
                                    location=location,
                                    #image=i
                                    image=image
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
