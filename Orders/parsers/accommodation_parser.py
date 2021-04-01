import Orders.api_models.models as api
from Orders.models.models import *

class AccommodationParser:

    def parse_accommodation_overview(self, accommodation):
        api_accommodation = api.Accommodation(
            id=accommodation.id.__str__(),
                location=api.Location(
                id=accommodation.location.id.__str__(),
                address=accommodation.location.address
            ),
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

        api_accommodation.rating.average /= api_accommodation.rating.count

        return api_accommodation
