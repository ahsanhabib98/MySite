from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.safestring import mark_safe
from .utils import get_read_time
from markdown_deux import markdown

# Create your models here.

class PostCategory(models.Model):
    name            = models.CharField(max_length=100)
    photo           = models.ImageField(upload_to='category_image', blank=True)
    brief           = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class PostModel(models.Model):
    draft           = models.BooleanField(default=False) #empty in the database
    title           = models.CharField(max_length = 300)
    slug            = models.SlugField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    read_time       = models.IntegerField(default=0)
    author_email    = models.EmailField(max_length=240)
    author_name     = models.CharField(max_length=200)
    updated         = models.DateTimeField(auto_now=True)
    photo           = models.ImageField(upload_to='blog_image')
    photo1          = models.ImageField(upload_to='blog_image', blank=True)
    category        = models.ForeignKey(PostCategory, on_delete=models.CASCADE)

    def __str__(self):
    	return self.title

    class Meta:
        ordering = ["-publish_date"]

    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)
    if instance.content:
        html_string = instance.get_markdown()
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var

pre_save.connect(pre_save_receiver, sender=PostModel)



def post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()

post_save.connect(post_save_receiver, sender=PostModel)
