from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profiles/')   # 👈 ImageField
    Descripstion = models.TextField(default="")
    def __str__(self):
        return self.name


#one to many

