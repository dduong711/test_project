from django.db import models
from django.contrib.auth import get_user_model

from mysite.users.models import User

class Organization(models.Model):
    name = models.CharField(max_length=256)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organization')
    
    def __str__(self):
        return self.name
