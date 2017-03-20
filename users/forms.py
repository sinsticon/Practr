from django import forms
from . models import student
from django.contrib.auth import (authenticate,login,logout,get_user_model)

user = get_user_model()

class RegisterModel(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = student
        fields = ['email','password','name','phoneno',]




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
               raise forms.ValidationError("Incorrent Username or Password")
            if not user.check_password(password):
              raise forms.ValidationError("Incorrent Password")