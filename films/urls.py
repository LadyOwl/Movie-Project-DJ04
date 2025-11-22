from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),      # /films/
    path('add/', views.add_film, name='add_film'),    # /films/add/
]