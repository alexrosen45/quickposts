from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    API_KEY_EXAMPLE = models.CharField(blank=True, unique=True, max_length=256)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, related_name='post_user')

    # human readable names
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
