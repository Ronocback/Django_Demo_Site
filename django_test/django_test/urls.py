from django.urls import path, include
from django.conf.urls import include, url
from django.contrib   import admin
from django_test import views 

urlpatterns = [
    path("", views.home, name="home"),
    path("quiz", include("quiz.urls")),
    url('admin/', admin.site.urls),
]