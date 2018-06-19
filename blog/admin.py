from django.contrib import admin
from .models import PostModel, PostCategory

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'draft',
        'title',
        'slug',
        'brief',
        'content',
        'photo',
        'photo1',
        'publish_date',
        'updated',
        'read_time',
        'author_email',
        'author_name',
        'category',
    ]

    readonly_fields = ['updated', ]

    class Meta:
        model = PostModel

admin.site.register(PostModel, PostModelAdmin)
admin.site.register(PostCategory)
