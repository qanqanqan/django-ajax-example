from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=30)
    enail = models.EmailField(max_length=100)
    is_staff = models.BooleanField(default=False)
