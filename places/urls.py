from django.urls import path
from places import views

urlpatterns = [
    path('', views.index),
    path('<int:id>/', views.about_place, name='place-json'),
]