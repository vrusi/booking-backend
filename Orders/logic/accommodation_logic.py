from Orders.parsers.accommodation_parser import AccommodationParser
from Orders.models import *


class AccommodationLogic:
    parser = AccommodationParser()

    def get_filtered_accommodations(self, filter_criteria):
        accommodations = Accommodation.objects.all()

        api_accommodations = [self.parser.parse_accommodation_overview(
            acc) for acc in accommodations]

        return api_accommodations

    def get_accommodation(self, pk):
        acc = Accommodation.objects.filter(id=pk)

        if len(acc) == 0:
            raise

        api_accommodation = self.parser.parse_accommodation_overview(acc[0])

        return api_accommodation

    def create_rating(self, user, acc_id, data):
        rating = Rating.objects.create(
            accommodation_id=acc_id,
            user=user,
            rating=data['rating'],
            title=data['title'],
            text=data['text']
        )

        if 'image' in data:
            uploaded_file_name = data['image'].name.split('.')[-1]

            file_name = f'rating_images/{rating.id.__str__()}'

            f = open(file_name, 'wb')
            f.write(data['image'].read())
            f.close()

    def update_rating(self, rating_id, data):
        # rating_id = data['id']

        try:
            rating = Rating.objects.filter(id=rating_id)[0]
        except Exception as e:
            raise e

        rating.rating = data['rating']
        rating.title = data['title']
        rating.text = data['text']

        rating.save()

    def delete_rating(self, rating_id):
        # rating_id = data['id']

        try:
            rating = Rating.objects.filter(id=rating_id)[0]
        except Exception as e:
            raise e

        rating.delete()

    def create_rating_reply(self, user, data):
        RatingReply.objects.create(
            rating_parent_id=data['parent'],
            user=user,
            text=data['text']
        )

    def update_rating_reply(self, reply_id, data):

        try:
            reply = RatingReply.objects.filter(id=reply_id)[0]
        except Exception as e:
            raise e

        reply.text = data['text']

        reply.save()

    def delete_rating_reply(self, reply_id):

        try:
            reply = RatingReply.objects.filter(id=reply_id)[0]
        except Exception as e:
            raise e

        reply.delete()
