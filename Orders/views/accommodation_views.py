import logging

from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny

from Orders.logic.accommodation_logic import AccommodationLogic


class AccommodationView(GenericViewSet):
    logger = logging.getLogger(__name__)
    logic = AccommodationLogic()

    permission_classes = [AllowAny]

    def list(self, request):
        try:
            filtered_accommodations = self.logic.get_filtered_accommodations(
                None)
            filtered_accommodations = [item.to_dict()
                                       for item in filtered_accommodations]
            pass
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(filtered_accommodations)

    def retrieve(self, request, pk):
        try:
            api_acc = self.logic.get_accommodation(pk)
            pass
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(api_acc.to_dict())

    @action(methods=['post'], detail=True, url_path='rating')
    def create_rating(self, request, pk):
        try:
            self.logic.create_rating(request.user, pk, request.data)
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(HTTP_200_OK)

    @action(methods=['put'], detail=True, url_path='rating/(?P<rating_id>.+)')
    def update_rating(self, request, pk, rating_id):
        try:
            self.logic.update_rating(rating_id, request.data)
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(HTTP_200_OK)

    @action(methods=['delete'], detail=True, url_path='rating/(?P<rating_id>.+)')
    def delete_rating(self, request, pk, rating_id):
        try:
            self.logic.delete_rating(rating_id)
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='rating_reply')
    def create_rating_reply(self, request, pk):
        try:
            self.logic.create_rating_reply(request.user, request.data)
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(HTTP_200_OK)

    @action(methods=['put'], detail=True, url_path='rating_reply/(?P<reply_id>.+)')
    def update_rating_reply(self, request, pk, reply_id):
        try:
            self.logic.update_rating_reply(reply_id, request.data)
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(HTTP_200_OK)

    @action(methods=['delete'], detail=True, url_path='rating_reply/(?P<reply_id>.+)')
    def delete_rating_reply(self, request, pk, reply_id):
        try:
            self.logic.delete_rating_reply(reply_id)
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='filter-criteria')
    def filter_criteria(self, request):
        return Response(HTTP_200_OK)
