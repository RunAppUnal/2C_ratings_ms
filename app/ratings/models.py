from django.db import models


class Rating(models.Model):
    class Meta:
        unique_together = (('route_id', 'user_id'),)

    RATINGS_CHOICES = (
        (1, 'Poor'),
        (2, 'Bad'),
        (3, 'Okay'),
        (4, 'Good'),
        (5, 'Great'),
    )

    # id = models.AutoField(primary_key=True)
    route_id = models.IntegerField(default=-1)
    user_id = models.IntegerField(default=-1)
    car_rating = models.IntegerField(default=-1, choices=RATINGS_CHOICES)
    driver_rating = models.IntegerField(default=-1, choices=RATINGS_CHOICES)
    average_rating = models.FloatField(default=0)
    comment = models.CharField(max_length=200)
