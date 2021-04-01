import logging


from django.db import transaction
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from rest_framework.response import Response

from .accommodation_fill import *


class FillView(GenericViewSet):
    permission_classes = [AllowAny]

    logger = logging.getLogger(__name__)

    @transaction.atomic
    def list(self, request):
        self.logger.debug("Calling DB fill")

        fill_accommodations()

        self.logger.debug("Ending DB fill")
        return Response('OK')
