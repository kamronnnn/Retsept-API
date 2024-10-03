from rest_framework.serializers import ModelSerializer
from .models import Food, Retsept, Comment



class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'



class RetseptSerializer(ModelSerializer):
    class Meta:
        model = Retsept
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

