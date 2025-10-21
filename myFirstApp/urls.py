from tempfile import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('myFirstApp/', views.apprenants, name='etudiants'),
    path('myFirstApp/details/<int:id>', views.details,name='details'),
    # path('', views.main, name='main'),
    path('template/', views.template_view, name='template'),
    path('', views.home, name='home'),
    path('accounts/inscription/', views.inscription, name='inscription'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),   
    path('accounts/profil_utilisateur/', views.profil_utilisateur ,name='profil_utilisateur'),   
    
    
    #les url pour le reset du mot de passe 
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='reset_password'),
    
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name='reset_password_sent'),
    
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'),
    
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name='password_reset_complete'),
    
]
