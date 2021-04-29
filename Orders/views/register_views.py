import logging

from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from Orders.logic.register_logic import RegisterLogic


class RegisterView(GenericViewSet):
    logger = logging.getLogger(__name__)
    logic = RegisterLogic()

    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False, url_path='register')
    def register(self, request):

        try:
            token = serializers.SerializerMethodField()
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            user = self.logic.register(request.data)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'token': token})
