from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Monitor(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    status = models.CharField(max_length=200,blank=False, default='')
    is_active = models.BooleanField(default=False)
    cpu_utilization = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
    )
    training_process = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
    )
    error_log = models.CharField(max_length=500, default='')

class Upload(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    path = models.CharField(max_length=200, blank=False, default='')
    created_at = models.DateTimeField()