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
            'categories': forms.CheckboxSelectMultiple(), 
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }

        
class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)


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

class ContactUsForm(forms.Form):
    Nom = forms.CharField(required=False)
    email = forms.CharField()
    message = forms.CharField(max_length=1000)