import logging


from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny

from Orders.logic.order_logic import OrderLogic


class OrderView(GenericViewSet):
    logger = logging.getLogger(__name__)
    logic = OrderLogic()

    # @action(methods=['get'], detail=False, url_path='orders')
    def list(self, request):
        try:
            api_orders = self.logic.get_list_orders(request.user)
            api_orders = [order.to_dict() for order in api_orders]

        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(api_orders)

    # @action(methods=['get'], detail=False, url_path='(/?P<order_id>.+)')
    def retrieve(self, request, pk):
        try:
            api_order = self.logic.get_order(request.user, pk)

        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(api_order.to_dict())

    @action(methods=['put'], detail=False, url_path='(?P<order_id>.+)/update')
    def update_order(self, request, order_id):
        try:
            api_order = self.logic.update_order(request.user, order_id, request.data)
            pass
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(api_order.to_dict())

    @action(methods=['delete'], detail=False, url_path='(?P<order_id>.+)/delete')
    def delete_order(self, request, order_id):
        try:
            self.logic.delete_order(request.user, order_id)
            pass
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='(?P<acc_id>.+)/create')
    def create_order(self, request, acc_id):
        try:
            self.logic.create_order(request.user, acc_id)
            pass
        except Exception as e:
            self.logger.exception(e)
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(HTTP_200_OK)
