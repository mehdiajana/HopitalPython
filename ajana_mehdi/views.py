from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *

# acceuil page
def acceuil(request):
    return render(request,'index.html')

# la liste des patients avec pagination de 10 par 10
def patients(request):
     patients = Patient.objects.all()
     paginator = Paginator(patients, 10)
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)
     title = 'liste des patients'
     context= {'patients': page_obj}
     return render(request, 'patients.html', context)

# la liste des medecins avec pagination de 10 par 10
def medecins(request):
     meds = Medecin.objects.all()
     paginator = Paginator(meds, 10)
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)
     title = 'liste des Medecins'
     context = {'medecins': page_obj}
     return render(request, 'medecins.html', context)

#pour afficher les détail d'un patient
def details(request, id):
    patient = Patient.objects.get(id = id)
    context = {'patient': patient}
    return render(request, 'detailsPatient.html',context)

# la liste des rendezvous d'un patient en passant l'ID
def rendezvouspatient(request, id):
     px = Patient.objects.get(id=id)
     rendezs = RendezVous.objects.all().filter(patient=px)
     title = 'liste des Rendez Vous dun patient'
     context = {'rendez': rendezs}
     return render(request, 'rendezvous.html', context)

# la liste des rendezvous
def rendezvous(request):
     rendezs = RendezVous.objects.all()
     title = 'liste des Rendez Vous'
     context = {'rendez': rendezs}
     return render(request, 'rendezvous.html', context)

# la liste des consultation
def consultation(request):
     consuls = RendezVous.objects.all()
     title = 'liste des Consultations'
     context = {'conc': consuls}
     return render(request, 'consultation.html', context)

# pour supprimer un patient et rediriger l'utilisateur vers la liste des patients
def deletePatient(request, id):
    try:
        patient = Patient.objects.get(id = id)
    except Patient.DoesNotExist:
        return redirect('/patients')
    patient.delete()
    return redirect('/patients')

# pour supprimer un medecin et rediriger l'utilisateur vers la liste des medecins
def deleteMedecin(request, id):
    try:
        medecin = Medecin.objects.get(id = id)
    except Patient.DoesNotExist:
        return redirect('/medecins')
    medecin.delete()
    return redirect('/medecins')

#pour afficher les détail d'un medecin
def detailsMedecin(request, id):
    medecin = Medecin.objects.get(id = id)
    context = {'medecin': medecin}
    return render(request, 'detailsMedecin.html',context)

#  Filter les patients en passant le nom
def search(request):
    naam = request.GET.get("name")
    patient = Patient.objects.all().filter(nom__contains=naam)
    title = 'liste des patients ayant un nom'
    context = {'patients': patient}
    return render(request, 'patients.html', context)




