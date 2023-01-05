from rest_framework.routers import DefaultRouter

from payment.api.views import HotelRoomAfterPaymentAPIView, FlightAfterPaymentAPIView

router = DefaultRouter()

router.register(r'payment/hotelroom', HotelRoomAfterPaymentAPIView, basename='paymenthotelroom')
router.register(r'payment/flight', FlightAfterPaymentAPIView, basename='paymentflight')


urlpatterns = [

]

urlpatterns += router.urls
