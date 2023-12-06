from django.shortcuts import render
from .models import Voiture

def voiture_list(request):
    voitures = Voiture.objects.all()
    return render(request, 'voitures/voiture_list.html', {'voitures':voitures})
# Create your views here.