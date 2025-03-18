from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Page de saisie d'email pour réinitialiser le mot de passe
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='authentication/password_reset.html'
         ), 
         name='password_reset'),

    # Confirmation d'envoi du mail
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='authentication/password_reset_done.html'
         ), 
         name='password_reset_done'),

    # Page de réinitialisation après clic sur lien dans email
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='authentication/password_reset_confirm.html'
         ), 
         name='password_reset_confirm'),

    # Confirmation de succès après modification du mot de passe
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='authentication/password_reset_complete.html'
         ), 
         name='password_reset_complete'),
]
