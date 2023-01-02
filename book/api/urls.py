from rest_framework.routers import DefaultRouter

from book.api.views import HotelRoomBookingViewSet

router = DefaultRouter()

router.register(r'hotelroombooking', HotelRoomBookingViewSet, basename='hotelroombooking')

urlpatterns = [

]

urlpatterns += router.urls
