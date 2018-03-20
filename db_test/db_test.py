from ratings.models import Rating
from ratings.serializers import RatingSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

rating = Rating(route_id=1, user_id=1, car_rating=4, driver_rating=3, average_rating=3.5, comment='I liked the travel')
rating.save()

rating = Rating(route_id=1, user_id=2, car_rating=5, driver_rating=3, average_rating=4, comment='The driver was awesome! I wanna marry him')
rating.save()

serializer = RatingSerializer(rating)
serializer.data

content = JSONRenderer().render(serializer.data)
content

from django.utils.six import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)
data

serializer = RatingSerializer(data=data)
serializer.is_valid()

serializer.validated_data

rating = serializer.save()
rating

rating.delete()

serializer = RatingSerializer(Rating.objects.all(), many=True)
serializer.data

from ratings.serializers import RatingSerializer

serializer = RatingSerializer()
print(repr(serializer))
