from django import forms
from .models import *
from pyuploadcare.dj.forms import ImageField

class ProfileForm(forms.ModelForm):

    class Meta: 
        model = Profile
        fields = ['name', 'current_city', 'avatar']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post 
        fields = ['title', 'content']