from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from django.urls import path



app_name = 'index'

urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    path('home/', views.Home.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('custom_login/', views.custom_login, name='custom_login'),
    path('create_user/', views.create_user, name='create_user'),




]
