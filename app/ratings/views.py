from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ratings.models import Rating
from ratings.serializers import RatingSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def rating_list(request):
    """
    List all code rating, or create a new rating.
    """
    if request.method == 'GET':
        ratings = Rating.objects.all()
        # print ratings
        serializer = RatingSerializer(ratings, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['average_rating'] = (data['car_rating'] + data['driver_rating']) / 2.0
        serializer = RatingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def rating_detail(request, pk):
    """
    Retrieve, update or delete a rating.
    """
    try:
        rating = Rating.objects.get(pk=pk)
    except Rating.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RatingSerializer(rating)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        data['average_rating'] = (data['car_rating'] + data['driver_rating']) / 2.0
        serializer = RatingSerializer(rating, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        rating.delete()
        return HttpResponse(status=204)
