from django.conf.urls import url,include
from . import views


app_name= 'users'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.user_logout, name='logout'),
    url(r'^user/', include('profile_page.urls')),
]
