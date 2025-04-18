from django import forms
from django.contrib.auth import get_user_model
from .models import Commentaire, Photo, Categorie, Blog
from . import models

User = get_user_model()

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption', 'categories'] 
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.CheckboxSelectMultiple(), 
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),

             'content': forms.Textarea(attrs={
                'rows': 10,
                'class': 'form-control',
                'placeholder': 'Rédigez votre contenu ici...'
            }),
            'categories': forms.CheckboxSelectMultiple(),
        }

        

class DeleteBlogForm(forms.Form):
    confirm = forms.BooleanField(label="Confirmer la suppression")


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']
        widgets = {
            'follows': forms.CheckboxSelectMultiple,
        }


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'placeholder': 'Laisser un commentaire...'}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Sujet', max_length=150)
    message = forms.CharField(label='Message', widget=forms.Textarea)