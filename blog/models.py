from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

# Create your models here.

class PostCategory(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='category_image', blank=True)

    def __str__(self):
        return self.name


class PostModel(models.Model):
    active          = models.BooleanField(default=True) #empty in the database
    title           = models.CharField(max_length = 300)
    slug            = models.SlugField(null=True, blank=True)
    brief           = models.CharField(max_length=500)
    content         = models.TextField(null=True, blank=True)
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email    = models.EmailField(max_length=240, null=True, blank=True)
    author_name     = models.CharField(max_length=200)
    updated         = models.DateTimeField(auto_now=True)
    photo           = models.ImageField(upload_to='blog_image', blank=True)
    category        = models.ForeignKey(PostCategory, on_delete=models.CASCADE)

    def __str__(self):
    	return self.title


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_receiver, sender=PostModel)



def post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()

post_save.connect(post_save_receiver, sender=PostModel)
