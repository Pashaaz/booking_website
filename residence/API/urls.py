from rest_framework.routers import DefaultRouter
from residence.API.views import HotelsViewSet

router = DefaultRouter()

router.register(r'hotels', HotelsViewSet, basename='hotels')

urlpatterns = [

]

urlpatterns += router.urls
