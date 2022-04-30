
from django.contrib import admin
from django.urls import path
from app import views
from app.views import RegisterAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book', views.viewbook),
    path('addbook', views.addbook),
    path('register/', RegisterAPI.as_view(), name='register')
]
