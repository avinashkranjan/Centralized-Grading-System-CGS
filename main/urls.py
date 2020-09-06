from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('index/', views.main_view, name="main_page"),
]