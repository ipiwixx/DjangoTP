from django.shortcuts import render
from .models import Voiture

def voiture_list(request):
    voitures = Voiture.objects.all()
    return render(request, 'car/voiture_list.html', {'voitures':voitures})

def voiture_detail(request, voiture_id):
    voiture = Voiture.objects.get(id=voiture_id)
    return render(request, 'car/voiture_detail.html', {'voiture':voiture})
# Create your views here.
