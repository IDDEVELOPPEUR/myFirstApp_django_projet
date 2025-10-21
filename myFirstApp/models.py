from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField

class Etudiant(models.Model):
  utilisateur = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
  prenom = models.CharField(max_length=255)
  nom = models.CharField(max_length=255)
  telephone=models.IntegerField(null=True)
  adresse=models.CharField(null=True,max_length=255)
  date=models.DateField(null=True)
  imageProfil=models.ImageField(null=True,default="profile1.png", blank=True)
  
  def __str__(self):
    return f"{self.prenom} {self.nom}"