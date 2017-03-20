from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.profile_page, name='profile_page'),
]
