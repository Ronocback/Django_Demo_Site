from django.urls import path, include
from django.conf.urls import include, url
from django.contrib   import admin
from django_test import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("quiz/", include("quiz.urls")),
    path('leaderboard/', include("leaderboard.urls")),
    url('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)