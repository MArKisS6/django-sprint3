from django.db import models


class VideoProduct(models.Model):
    title = models.CharField(max_length=128)
