from Orders.parsers.accommodation_parser import AccommodationParser
from Orders.models import *

class AccommodationLogic:
    parser = AccommodationParser()

    def get_accommodation(self, pk):
        acc = Accommodation.objects.filter(id=pk)

        if len(acc) == 0:
            raise

        api_accommodation = self.parser.parse_accommodation_overview(acc[0])

        return api_accommodation
