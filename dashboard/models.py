from django.db import models
from django.contrib.auth.models import User

class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quick_links = models.JSONField(default=list)
    notifications = models.JSONField(default=list)

    def __str__(self):
        return f"{self.user.username}'s Dashboard"
