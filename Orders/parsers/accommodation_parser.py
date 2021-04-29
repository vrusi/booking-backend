import Orders.api_models.models as api
import os.path
from Orders.models.models import *


class AccommodationParser:

    def parse_accommodation_overview(self, accommodation):
        api_accommodation = api.Accommodation(
            id=accommodation.id.__str__(),
            location=api.Location(
                id=accommodation.location.id.__str__(),
                address=accommodation.location.address
            ),
            description=accommodation.description,
            images=accommodation.images,
            title=accommodation.title,
            occupant_count=accommodation.occupant_count
        )

        # Rating
        api_accommodation.rating = api.AccommodationRating(
            average=0.0,
            count=0,
        )

        api_accommodation.rating.ratings = [
            self.parse_and_count_ratings(api_accommodation.rating, rating)
            for rating
            in Rating.objects.filter(accommodation=accommodation)
        ]

        api_accommodation.rating.average = None if api_accommodation.rating.count == 0 else api_accommodation.rating.average / \
            api_accommodation.rating.count

        return api_accommodation

    def _count_ratings(self, acc_rating, rating):
        acc_rating.average += rating.rating
        acc_rating.count += 1

    def parse_and_count_ratings(self, object_rating, rating):

        file_name = f'rating_images/{rating.id.__str__()}.jpg'

        image = file_name if os.path.exists(file_name) else None

        api_rating = api.Rating(
            id=rating.id.__str__(),

            author=api.User(
                username=rating.user.username,
                first_name=rating.user.first_name,
                last_name=rating.user.last_name,
            ),
            image=image,

            rating=rating.rating,
            title=rating.title,
            content=rating.text,
            created_at=rating.created_at.isoformat(),

        )

        api_rating.replies = [api.RatingReply(
            id=reply.id.__str__(),

            author=api.User(
                username=reply.user.username,
                first_name=reply.user.first_name,
                last_name=reply.user.last_name,
            ),

            content=reply.text,
            created_at=reply.created_at,
        ) for reply in RatingReply.objects.filter(rating_parent=rating)]

        object_rating.average += rating.rating
        object_rating.count += 1

        return api_rating
