from django.conf.urls import url
from .views import* 


urlpatterns = [
    url(r'^blog_list/', blog_list, name = 'blog_list'),
    url(r'^blog_detail/(?P<id>\d+)/', blog_detail, name = 'blog_detail'),
    
]
