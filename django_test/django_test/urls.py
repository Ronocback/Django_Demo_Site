from django.urls import path, include
from django_test import views 

urlpatterns = [
    path("", views.home, name="home"),
    path("quiz", include("quiz.urls"))
]