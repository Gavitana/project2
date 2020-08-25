from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files import File
from urllib import request
import os


class User(AbstractUser):
    pass


class Categories(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"


class Listing(models.Model):
    name = models.CharField(max_length=64,null=True)
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="types")
    image_url = models.URLField()
    bid = models.IntegerField()

    def get_remote_image(self):
        if self.image_url == True:
            result = request.urlretrieve(self.image_url)
            self.image_file.save(
                os.path.basename(self.image_url),
                File(open(result[0], 'rb'))
                )
            self.save()

    def __str__(self):
        return f"{self.name}"
