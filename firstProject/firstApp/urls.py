from django.urls import path
from . import views

urlpatterns = [
    path('emps/', views.employeeView, name='home'),
]
