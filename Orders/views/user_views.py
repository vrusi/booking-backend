import logging

from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny

from Orders.logic.user_logic import UserLogic


class UserView(GenericViewSet):
    logger = logging.getLogger(__name__)
    logic = UserLogic()

    # permission_classes = [AllowAny]

    @action(methods=['get'], detail=False, url_path='get')
    def get_user_info(self, request):
        try:
            api_user = self.logic.get_user_info(request.user.id)
            pass
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(api_user.to_dict())

    @action(methods=['put'], detail=False, url_path='update')
    def update_user_info(self, request):
        try:
            api_user = self.logic.update_user_info(request.user.id, request.data)
            pass
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(api_user.to_dict())

    @action(methods=['delete'], detail=False, url_path='delete')
    def delete_user(self, request):
        try:
            api_user = self.logic.delete_user(request.user.id)
            pass
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(HTTP_200_OK)