from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'route_id', 'user_id', 'car_rating', 'driver_rating', 'average_rating', 'comment')
