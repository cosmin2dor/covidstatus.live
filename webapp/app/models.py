from django.db import models


class Subscription(models.Model):
    email = models.EmailField(max_length=100)
    country_name = models.CharField(max_length=100)


class Message(models.Model):
    message = models.CharField(max_length=500, blank=False)
    date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)