from Orders.models import *

import random


def fill_locations():
    for i in range(5):
        Location.objects.create(
            address='Adresa lokácie ' + str(i)
        ).save()

    return Location.objects.all()


def fill_accommodations():
    locations = fill_locations()

    for i in range(10):
        Accommodation.objects.create(
            title='Názov ubytovania ' + str(i),
            description="Popis ubytovania " + str(i),
            images=('https://images.unsplash.com/photo-1597047084897-51e81819a499?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80', 'https://images.unsplash.com/photo-1603794067602-9feaa4f70e0c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80'),
            occupant_count=random.randint(2,10),
            location=random.choice(locations)
        ).save()

    return Accommodation.objects.all()


