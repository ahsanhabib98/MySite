from django.conf.urls import url
from .views import* 


urlpatterns = [
    url(r'^service_list/', service_list, name = 'service_list'),
    url(r'^service_detail/(?P<id>\d+)/', service_detail, name = 'service_detail'),
    
]
