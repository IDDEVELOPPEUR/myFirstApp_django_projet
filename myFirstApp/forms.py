# your_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms as form
from .models import Etudiant



class FormulaireInscription(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class EtudiantForm(ModelForm):
        class Meta:
            model = Etudiant
            fields = "__all__"
            exclude = ['utilisateur']
    