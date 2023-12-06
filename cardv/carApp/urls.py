from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('voitures/', views.voiture_list, name="voitures"),
    path('voiture/<int:voiture_id>/', views.voiture_detail, name="voiture")

]
