from django.db import models

class Voiture(models.Model):
    marque = models.CharField(max_length=200)
    modele = models.CharField(max_length=200)
    anneeConstruction = models.DateTimeField()
    cylindree = models.IntegerField()
    version = models.CharField(max_length=200)
    #note = models.IntegerField()

    def __str__(self):
        return self.marque