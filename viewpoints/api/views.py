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
                          # mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    queryset = HotelComment.objects.all()
    authentication_classes = [JWTAuthentication]
    serializer_class = HotelCommentSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     if self.action == 'list':
    #         queryset = HotelComment.objects.all().filter(hotel_id=request.data.get())


class CompanyCommentViewSet(mixins.CreateModelMixin,
                            # mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = CompanyComment.objects.all()
    authentication_classes = [JWTAuthentication]
    serializer_class = HotelCommentSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     if self.action == 'list':
    #         queryset = HotelComment.objects.all().filter(hotel_id=request.data.get())


class HotelRatingViewSet(mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         # mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = HotelRating.objects.all()
    authentication_classes = [JWTAuthentication]
    serializer_class = HotelCommentSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     if self.action == 'list':
    #         queryset = HotelComment.objects.all().filter(hotel_id=request.data.get())


class CompanyRatingViewSet(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           # mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    queryset = CompanyRating.objects.all()
    authentication_classes = [JWTAuthentication]
    serializer_class = HotelCommentSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     if self.action == 'list':
    #         queryset = HotelComment.objects.all().filter(hotel_id=request.data.get())
