from django import forms
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']


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

class ContactUsForm(forms.Form):
    Nom = forms.CharField(required=False)
    email = forms.CharField()
    message = forms.CharField(max_length=1000)