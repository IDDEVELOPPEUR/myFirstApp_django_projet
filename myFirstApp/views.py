from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Etudiant
from django.contrib.auth.models import Group
from .forms import EtudiantForm, FormulaireInscription

def inscription(request):
    form = FormulaireInscription()
    if request.method == 'POST':
        form = FormulaireInscription(request.POST)
        if form.is_valid():
            new_user= form.save()
            
            Etudiant.objects.create(
                #association d'un profil vide à tout nouvel inscrit !      
                utilisateur=new_user,
            )
            
            # c'est ce qui permet de placer tout nouvel étudiant dans un groupe !
            group_etudiant=Group.objects.get(name="etudiant")
            new_user.groups.add(group_etudiant)
            
            user = form.cleaned_data.get('username')
            messages.success(request, 'Le compte a été créé pour ' + user)
            return redirect('login') 
    return render(request, 'inscription.html', {'formulaire': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('login')  
        password = request.POST.get('password')
        utilisateur = authenticate(request, username=username, password=password)
        if utilisateur is not None:
            auth_login(request, utilisateur) 
            return redirect('home')
        else:
            messages.info(request, 'Login ou mot de passe incorrect')
    return render(request, 'login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def apprenants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiants.html', {'etudiants': etudiants})


def profil_utilisateur(request):
    etudiant=request.user.etudiant
    formulaire=EtudiantForm(instance=etudiant)
    if request.method=='POST':
        formulaire=EtudiantForm(request.POST,request.FILES,instance=etudiant)
        if formulaire.is_valid():
            formulaire.save()
            # return redirect('profil_utilisateur')
    context={'formulaire':formulaire}
    return render(request, 'profil_utilisateur.html',context)


def details(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    return render(request, 'details.html', {'etudiant': etudiant})

def home(request):
    return render(request, 'home.html')

def main(request):
    return render(request, 'main.html')

def template_view(request):
    mesdonnees = Etudiant.objects.all()
    donneesfiltres = Etudiant.objects.filter(prenom='Ibrahima')
    nomdonnees = Etudiant.objects.filter(prenom__startswith='I')
    ordonnees = Etudiant.objects.all().order_by('nom')
    context = {
        'mesdonnees': mesdonnees,
        'donneesfiltres': donneesfiltres,
        'nomdonnees': nomdonnees,
        'ordonnees': ordonnees,
    }
    return render(request, 'template.html', context)

def profile(request):
    return render(request, 'profile.html')