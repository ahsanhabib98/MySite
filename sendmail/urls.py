from django.conf.urls import url
from .views import*
urlpatterns = [
    url(r'^email/', emailview, name='email'),
    url(r'^success/', successview, name='success'),
]
