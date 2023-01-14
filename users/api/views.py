from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.api.serializers import ProfileSerializer, CustomUserSerializer, LoginFirstSerializer, LoginSecondSerializer
from users.models import UserProfile, CustomUser
from utils.utils import get_tokens_for_user, otp_gen


class UserProfileViewSet(mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):

    queryset = UserProfile.objects.all().prefetch_related('user',)
    serializer_class = ProfileSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]


class UserViewSet(
            mixins.CreateModelMixin,
            mixins.ListModelMixin,
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin,
            mixins.RetrieveModelMixin,
            viewsets.GenericViewSet
            ):

    authentication_classes = [JWTAuthentication]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]

        elif self.action == 'list':
            return [IsAdminUser()]

        elif self.action == 'update':
            return [IsAuthenticated()]


class LoginFirstAPIView(GenericAPIView):
    serializer_class = LoginFirstSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            email = request.data['email']
            code = otp_gen()
            cache.set(str(email), code, 120)

            return Response({"code": code})


class LoginSecondAPIView(GenericAPIView):
    serializer_class = LoginSecondSerializer

    def post(self, request):
        email = request.data['email']
        user_answer = request.data['code']
        code = cache.get(str(email))

        if user_answer == code:
            try:
                user = CustomUser.objects.get(email=email)
                token = get_tokens_for_user(user)
                return Response(token)

            except ObjectDoesNotExist:
                return Response('User not found')

        else:
            return Response('Wrong Code')
