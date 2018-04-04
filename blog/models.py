from django.db import models
from django.utils import timezone 

# Create your models here.


class PostModel(models.Model):
    active          = models.BooleanField(default=True) #empty in the database
    title           = models.CharField(max_length = 300)
    slug            = models.SlugField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email    = models.EmailField(max_length=240, null=True, blank=True)
    updated         = models.DateTimeField(auto_now=True)
    photo           = models.ImageField(upload_to='blog_image', blank=True)
    
    def __str__(self):
    	return self.title
