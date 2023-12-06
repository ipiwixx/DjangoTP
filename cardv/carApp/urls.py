from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('voitures/', views.voiture_list, name="voitures")
]
