from Orders.models.models import *
from Orders.parsers.order_parser import OrderParser


class OrderLogic:
    parser = OrderParser()

    def get_list_orders(self, user):
        try:
            orders = Order.objects.filter(booked_by=user)
        except Exception as e:
            raise e

        api_orders = [self.parser.parse_order(order) for order in orders]
        return api_orders

    def get_order(self, user, order_id):
        try:
            order = Order.objects.filter(booked_by=user, id=order_id)[0]
        except Exception as e:
            raise e

        api_order = self.parser.parse_order(order)
        return api_order

    def create_order(self, user, acc_id):
        try:
            Order.objects.create(
                acc_booked_id=acc_id,
                booked_by=user
            )
        except Exception as e:
            raise e

    def update_order(self, user, order_id, data):
        try:
            order = Order.objects.filter(booked_by=user, id=order_id)[0]
        except Exception as e:
            raise e

        order.acc_booked_id = data['acc_id']

        order.save()

        api_order = self.parser.parse_order(order)
        return api_order

    def delete_order(self, user, order_id):
        try:
            order = Order.objects.filter(booked_by=user, id=order_id)[0]
        except Exception as e:
            raise e

        order.delete()
