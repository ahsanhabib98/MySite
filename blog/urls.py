from django.conf.urls import url
from .views import*


urlpatterns = [
    url(r'^blog_create/', blog_create, name = 'blog_create'),
    url(r'^blog_list/', blog_list, name = 'blog_list'),
    url(r'^blog_detail/(?P<id>\d+)/', blog_detail, name = 'blog_detail'),
    url(r'^category/', category, name = 'category'),
    url(r'^categorywise_blog/(?P<id>\d+)/', categorywise_blog, name = 'categorywise_blog'),

]
