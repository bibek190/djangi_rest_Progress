
from django.urls import path
from .views import studentsView,studentDetailView,EmployeeView

urlpatterns = [
    path("students/",studentsView),
    path("students/<int:pk>/",studentDetailView),
    path("employees/",EmployeeView.as_view())
    
]