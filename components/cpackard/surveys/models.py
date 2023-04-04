# Django Libraries
from django.db import models


class Survey(models.Model):
    satisfaction = models.IntegerField(default=0)
    response_text = models.CharField(max_length=200)
