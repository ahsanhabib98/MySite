from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='service_image', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    updated_date = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.title
