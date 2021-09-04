from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=150, label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=150, label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=150, label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', )
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': f'{Todo._meta.get_field("title").verbose_name}'})
        }