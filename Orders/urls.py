from rest_framework.routers import DefaultRouter
from Orders.views.accommodation_views import AccommodationView
from Orders.views.register_views import RegisterView
from Orders.views.user_views import UserView
from Orders.views.order_views import OrderView

from Orders.tests.fill.fill_view import FillView


router = DefaultRouter()
router.register(r'accommodation', AccommodationView, basename='accommodation')
router.register(r'auth', RegisterView, basename='auth')
router.register(r'user', UserView, basename='user')
router.register(r'order', OrderView, basename='order')

router.register(r'fill', FillView, basename='fill')  # for testing purposes

urlpatterns = router.urls
