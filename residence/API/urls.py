from rest_framework.routers import DefaultRouter
from residence.API.views import HotelsViewSet, HotelRoomViewSet

router = DefaultRouter()

router.register(r'hotels', HotelsViewSet, basename='hotels')
router.register(r'hotelrooms', HotelRoomViewSet, basename='hotelrooms')

urlpatterns = [

]

urlpatterns += router.urls
