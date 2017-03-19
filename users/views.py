from django.shortcuts import render
from . models import student
from .forms import RegisterModel,LoginForm
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    form = RegisterModel(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        username=form.cleaned_data['username']
        new_user_test,created = student.objects.get_or_create(username=username)
        if created:
            new_user.save()
    formin = LoginForm(request.POST or None)
    if formin.is_valid():
        username = formin.cleaned_data.get("username")
        password = formin.cleaned_data.get("password")
    context={"form":form, "formin":formin}
    return render(request,'home/index.html',context)


def user_page(request):
    context={}
    return render(request,'user_page/user_page.html',context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username= form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    context ={"form":form}