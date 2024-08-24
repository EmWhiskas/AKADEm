from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import *

class FormRegister(UserCreationForm):
    username = forms.CharField(label='Логин', help_text='')
    password1 = forms.CharField(label='Пароль', help_text='',
                                widget=forms.PasswordInput(
                                    attrs={'autocomplete':'new-password'}
                                ))
    password2 = forms.CharField(label='Подтверждение пароля', help_text='',
                                widget=forms.PasswordInput(
                                    attrs={'autocomplete':'new-password'}
                                ))
    email = forms.EmailField(label='Почта',
                             widget=forms.TextInput(
                                 attrs={'placeholder':'qwe@mail.ru'}
                             ))
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)

class AddFile(forms.Form):
    # STAT = (("Ф", 'Фото'), ("В", 'Видео'), ("Д", 'Документы'))
    # name = forms.CharField(label='Название файла', required=True)
    file = forms.FileField(label='Файл')
    # img = forms.FileField(label='Картинка', required=False)
    # category = forms.ChoiceField(label='Категория файла', choices=STAT)

class AddGb(forms.Form):
    gb = forms.ModelChoiceField(Storage.objects.all(), label='Выберете')