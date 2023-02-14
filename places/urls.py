from django.urls import path
from places import views

urlpatterns = [
    path('', views.index),
    path('place/<int:id>/', views.about_place),
]