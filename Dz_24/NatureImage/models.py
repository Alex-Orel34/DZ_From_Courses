from django.db import models
from django.contrib import admin


class NatureImage(models.Model):
    url = models.URLField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    desc = models.CharField(max_length=255)


admin.site.register(NatureImage)
