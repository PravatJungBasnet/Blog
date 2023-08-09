from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import post
class signup(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput (attrs={'class':'form-control'}))
   
    class Meta:
        model=User
        fields=['username','email']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control',}), 'email':forms.EmailInput(attrs={'class':'form-control'})}
class Postform(forms.ModelForm):
    class Meta:
        model=post
        fields=['id','Tittle','desc']
        labels={'desc':'Description'}
        widgets={'Tittle':forms.TextInput(attrs={'class':'form-control'}),'desc':forms.Textarea(attrs={'class':'form-control'})}

       
       


    

    