from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields="__all__"

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields="__all__"

class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('comment',)     

        labels={
            'comment':'comment',
            
        }

        widgets={
           'comment': forms.TextInput(attrs={'class': 'form-control','placeholder':'comment'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields = '__all__'

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email','password1','password2')
    def __init__(self, *args,**kwargs):
        super(RegisterUserForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'