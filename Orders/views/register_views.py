import logging

from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny

from Orders.logic.register_logic import RegisterLogic


class RegisterView(GenericViewSet):
    logger = logging.getLogger(__name__)
    logic = RegisterLogic()

    permission_classes = [AllowAny]


    @action(methods=['post'], detail=False, url_path='register')
    def register(self, request):
        try:
            self.logic.register(request.data)
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(HTTP_200_OK)











