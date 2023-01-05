from rest_framework.routers import DefaultRouter

from payment.api.views import HotelRoomAfterPaymentAPIView, FlightAfterPaymentAPIView

router = DefaultRouter()

router.register(r'hotelroom', HotelRoomAfterPaymentAPIView, basename='hotelroom')
router.register(r'flight', FlightAfterPaymentAPIView, basename='flight')


urlpatterns = [

]

urlpatterns += router.urls
