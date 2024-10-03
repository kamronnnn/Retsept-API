from rest_framework import viewsets
from .models import Food, Retsept, Comment
from .serializers import FoodSerializer, RetseptSerializer, CommentSerializer

# Create your views here.

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class RetseptViewSet(viewsets.ModelViewSet):
    queryset = Retsept.objects.all()
    serializer_class = RetseptSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
