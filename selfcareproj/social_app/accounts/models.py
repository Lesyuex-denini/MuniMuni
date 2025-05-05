from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined = models.DateField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return self.user.username
