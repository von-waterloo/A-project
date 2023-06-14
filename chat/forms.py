from django import forms

class AuthForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)