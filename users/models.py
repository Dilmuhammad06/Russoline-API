from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='images/users/',default='images/users/default_user.png')
    about = models.CharField(max_length=255,default="")
    visable = models.BooleanField(default=True)