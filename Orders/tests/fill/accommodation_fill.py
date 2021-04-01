from Orders.models import *

import random


def fill_locations():
    for i in range(5):
        Location.objects.create(
            address='Adresa lokácie' + str(i)
        ).save()

    return Location.objects.all()


def fill_accommodations():
    locations = fill_locations()

    for i in range(10):
        Accommodation.objects.create(
            location=random.choice(locations)
        ).save()

    return Accommodation.objects.all()


