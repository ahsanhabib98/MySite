from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^email/', views.emailview, name='email'),
    url(r'^success/', views.successview, name='success'),
]
