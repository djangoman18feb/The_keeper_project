from django.contrib.auth.models import User #we need to have access of model - User class
from django import forms


class Userform(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']