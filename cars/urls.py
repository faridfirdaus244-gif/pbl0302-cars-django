from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('create/', views.car_create, name='car_create'),
    path('update/<int:pk>/', views.car_update, name='car_update'),
    path('delete/<int:pk>/', views.car_delete, name='car_delete'),
]