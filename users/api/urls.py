from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    path('login/first/', LoginFirstAPIView.as_view(), name="first"),
    path('login/second/', LoginSecondAPIView.as_view(), name="second")
]

urlpatterns += router.urls
