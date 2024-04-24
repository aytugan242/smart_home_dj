from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    sensor_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default=None)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='sensor', on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(max_length=100, null=True)
