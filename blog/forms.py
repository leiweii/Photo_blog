from django import forms
from django.contrib.auth import get_user_model
from .models import Commentaire, Photo, Categorie
from . import models

User = get_user_model()

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption', 'categorie']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name']


class BlogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
    class Meta:
        model = models.Blog
        fields = ['title', 'content']
        # fields = '__all__'
        
        
class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']
        widgets = {
            'follows': forms.CheckboxSelectMultiple,
        }


# class PhotoCommentForm(forms.ModelForm):
#     class Meta:
#         model = PhotoComment
#         fields = ['text']


from django import forms
from .models import Commentaire

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