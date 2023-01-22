from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ACCESS_TOKEN = models.CharField(blank=True, unique=True, max_length=256)
    ACCESS_SECRET = models.CharField(blank=True, unique=True, max_length=256)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, related_name='user_profile')

    # human readable names
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
