from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Aluno, Casa, Animal, Varinha, Madeira, Tamanho, Nucleo, Personagem

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class AlunoManagerForm(models.Manager):
    def create_list(self, user):
        new_list = self.model(usuario=user)
        new_list.save()
        return new_list

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ['usuario']
    
    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario')
        super(AlunoForm, self).__init__(*args, **kwargs)