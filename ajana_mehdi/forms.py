from django import forms

class rechercheForm(forms.Form):
    recherche_input = forms.CharField()

class PatientForm (forms.Form):
    nom_input = forms.CharField()
    prenom_input = forms.CharField()
    email_input = forms.EmailField()
    ddn_input = forms.DateField()

class MedecinForm (forms.Form):
    nom_input = forms.CharField()
    prenom_input = forms.CharField()
    specialite_input = forms.CharField()

class RendezVousForm (forms.Form):
    date_input = forms.DateField()
    annuler_input = forms.BooleanField()
    patientid_input = forms.IntegerField()
    medecinid_input = forms.IntegerField()

class ConsultationForm (forms.Form):
    description_input = forms.CharField()
    traitement_input = forms.CharField()
    type_input = forms.CharField()
    rdvid_input = forms.IntegerField()

