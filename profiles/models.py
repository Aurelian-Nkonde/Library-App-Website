from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to="profile_pics")
    city = models.CharField(max_length=200)


    def __str__(self):
        return "{0}".format(self.user.username)