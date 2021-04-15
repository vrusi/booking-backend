import uuid
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField



class AbstractModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(AbstractUser, AbstractModel):

    class Meta:
        db_table = 'UserProfile'


class Location(AbstractModel):
    address = models.CharField(max_length=100)

    class Meta:
        db_table = 'Location'


class Accommodation(AbstractModel):
    title = models.CharField(max_length=512)
    description= models.CharField(max_length=512)
    occupant_count = models.IntegerField(null=False, default=0)

    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False)
    images = ArrayField(models.CharField(max_length=150, blank=False))
    class Meta:
        db_table = 'Accommodation'


class Order(AbstractModel):
    class State(models.TextChoices):
        CREATED = 'Created'
        PAID = 'Paid'

    booked_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)
    acc_booked = models.ForeignKey(Accommodation, on_delete=models.CASCADE, null=False)
    occupant_count = models.IntegerField(null=True, default=0)

    state = models.CharField(
        max_length=10,
        choices=State.choices,
        default=State.CREATED
    )

    class Meta:
        db_table = 'Order'


class Rating(AbstractModel):
    rating = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=512)
    text = models.TextField(null=True)

    class Meta:
        db_table = 'Rating'


class RatingReply(AbstractModel):
    rating_parent = models.ForeignKey(Rating, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)
    text = models.TextField(null=True)

    class Meta:
        db_table = 'RatingReply'
