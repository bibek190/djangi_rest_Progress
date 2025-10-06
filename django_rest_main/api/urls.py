
from django.urls import path
from .views import studentsView,studentDetailView

urlpatterns = [
    path("students/",studentsView),
    path("students/<int:pk>/",studentDetailView),
    
]