from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from pyuploadcare.dj.models import ImageField

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    photo = ImageField(blank=True, manual_crop="")

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=75)
    current_city = models.CharField(max_length=100)
    avatar = ImageField(blank=True, manual_crop="")
    join_date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
