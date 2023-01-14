from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from viewpoints.api.serializers import (
    HotelCommentSerializer,
    CompanyCommentSerializer,
    HotelRatingSerializer,
    CompanyRatingSerializer,
)
from viewpoints.models import (
    HotelComment,
    CompanyComment,
    HotelRating,
    CompanyRating,
)


class HotelCommentViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):

    authentication_classes = [JWTAuthentication]
    serializer_class = HotelCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = HotelComment.objects.all()

        if self.action == 'list':
            queryset = HotelComment.objects.all().filter(hotel_id=self.request.data.get('hotel'))


class CompanyCommentViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = CompanyCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CompanyComment.objects.all()

        if self.action == 'list':
            queryset = CompanyComment.objects.all().filter(hotel_id=self.request.data.get('hotel'))


class HotelRatingViewSet(mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = HotelRatingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = HotelRating.objects.all()

        if self.action == 'list':
            queryset = HotelRating.objects.all().filter(hotel_id=self.request.data.get('hotel'))


class CompanyRatingViewSet(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = CompanyRatingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CompanyRating.objects.all()

        if self.action == 'list':
            queryset = CompanyRating.objects.all().filter(hotel_id=self.request.data.get('hotel'))
