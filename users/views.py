from django.shortcuts import render
from . models import student
from .forms import RegisterModel


# Create your views here.

def index(request):
    form = RegisterModel(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        username=form.cleaned_data['username']
        new_user_test,created = student.objects.get_or_create(username=username)
        if created:
            new_user.save()
    context={"form":form}
    return render(request,'home/index.html',context)

