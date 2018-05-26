from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    photo = models.ImageField(upload_to='author_image', blank=True)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email
