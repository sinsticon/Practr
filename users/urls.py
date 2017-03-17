from django.conf.urls import url
from . import views


app_name= 'users'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^[pk]$', views.user_page,name='user_page'),  #take the user pk here
]
