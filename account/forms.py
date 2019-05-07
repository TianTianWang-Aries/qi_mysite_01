# _*_ coding:utf-8 _*_
__author__ = "Aries"
__date__ = "DATE 18:50"
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
