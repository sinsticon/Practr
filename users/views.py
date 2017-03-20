from django.shortcuts import render
from . models import student
from .forms import RegisterModel,LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from .models import student as User


# Create your views here.

def index(request):
    form = RegisterModel(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data['email']
        password=form.cleaned_data['password']
        name = form.cleaned_data['name']
        phoneno = form.cleaned_data['phoneno']
        new_user=User.objects.create_user(username,password,name,phoneno)
        if new_user.save():
            return HttpResponse("<h1>Logged in</h1>")

    formin = LoginForm(request.POST or None)
    if formin.is_valid():
        username = formin.cleaned_data.get("username")
        password = formin.cleaned_data.get("password")
        user = auth.authenticate(email=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponse("<h1>Logged in</h1>")
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