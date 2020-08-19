from django.db import models


# Create your models here.
class Tours(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    departure = models.CharField(max_length=10)
    picture = models.TextField()
    price = models.IntegerField()
    stars = models.IntegerField()
    country = models.CharField(max_length=150)
    nights = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.title}'
