from django.urls import path
from .views import (
    class_view,
    # class_add,
)

urlpatterns = [
    path('', class_view, name="class_page"),
]