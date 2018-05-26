from django.contrib import admin
from .models import PostModel, PostCategory

# Register your models here.

admin.site.register(PostModel)
admin.site.register(PostCategory)
