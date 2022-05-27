from django.db import models

# Create your models here.
class Patient(models.Model):
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    email = models.EmailField(max_length=100)
    dateNaissance = models.DateField(null=True)

    def __str__(self):
        return self.nom

class Medecin(models.Model):
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    specialite = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class RendezVous(models.Model):
    dateRendezvous = models.DateField(null=True)
    annuler = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)


class Consultation(models.Model):
    description = models.CharField(max_length=200)
    traitement = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=60)
    rendezvous = models.OneToOneField(RendezVous, on_delete=models.CASCADE)

