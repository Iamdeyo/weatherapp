
from django.urls import path
from .views import addCity, delCity, index

urlpatterns = [
    path('', index, name='index'),
    path('add/', addCity, name='add'),
    path('delete/<str:cn>', delCity, name='del'),
]
