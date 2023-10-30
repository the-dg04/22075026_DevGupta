from django.db import models
from django.conf import settings

class UrlMap(models.Model):
    long_url=models.CharField(max_length=200)
    short_url=models.CharField(max_length=200)

    def get_short_url(self):
        return settings.BASE_URL+"/urls/"+self.short_url

