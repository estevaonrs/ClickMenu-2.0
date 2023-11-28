from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.Index.as_view())
]
