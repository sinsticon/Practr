from django.forms import ModelForm
from . models import student


class RegisterModel(ModelForm):
    class Meta:
        model = student
        fields = ['name','username','phoneno','password']