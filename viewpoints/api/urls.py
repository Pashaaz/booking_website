from rest_framework.routers import DefaultRouter

from viewpoints.api.views import (
    HotelCommentViewSet,
    CompanyCommentViewSet,
    HotelRatingViewSet,
    CompanyRatingViewSet,
)

router = DefaultRouter()

router.register(r'hotel/comment', HotelCommentViewSet, basename='hotel/comment')
router.register(r'hotel/rating', HotelRatingViewSet, basename='hotel/rating')
router.register(r'company/comment', CompanyCommentViewSet, basename='company/comment')
router.register(r'company/rating', CompanyRatingViewSet, basename='company/rating')


urlpatterns = [

]

urlpatterns += router.urls
