from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import FoodViewSet, RetseptViewSet, CommentViewSet

router = SimpleRouter()

router.register(r'foods', FoodViewSet, basename='food')
router.register(r'retsepts', RetseptViewSet, basename='retsept')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
