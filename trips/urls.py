from django.urls import path
from . import views

urlpatterns = [
    path('', views.trip_list, name='trip_list'),
    path('new/', views.trip_new, name='trip_new'),
    path('edit/<int:trip_id>/', views.trip_edit, name='trip_edit'),
    path('delete/<int:trip_id>/', views.trip_delete, name='trip_delete'),
]



