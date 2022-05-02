
from django.urls import path
from .views import addCity, index

urlpatterns = [
    path('', index, name='index'),
    path('add/', addCity, name='add'),
]
