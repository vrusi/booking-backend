
import Orders.api_models.models as api

class OrderParser:

    def parse_order(self, order):
        api_order = api.Order(
            id=order.id.__str__(),
            state=order.state,
            accommodation=order.acc_booked.id.__str__(),
            occupant_count=order.occupant_count
        )

        return api_order