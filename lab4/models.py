from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class VoltageSample(models.Model):
    data = ArrayField(models.FloatField())
    name = models.CharField(max_length=50, default="Unspecified")
    freq = models.IntegerField(default=10)
    raw = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)
