# from django import forms

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=63, label='Nom d’utilisateur')
#     password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    # Classe Meta pour spécifier des options supplémentaires
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')


class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_photo', )