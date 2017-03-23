from django.shortcuts import render
from . models import student
from .forms import RegisterModel,LoginForm, MoreInfo
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
        new_user.save()
    formin = LoginForm(request.POST or None)
    if formin.is_valid():
        username = formin.cleaned_data.get("username")
        password = formin.cleaned_data.get("password")
        user = auth.authenticate(email=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.activated:
                return HttpResponseRedirect('/profile_page/')
            else:
                return HttpResponseRedirect('/home/personal_info/')
    context={"form":form, "formin":formin}
    return render(request,'home/index.html',context)


def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/home/')

def personal_info(request):
    form = MoreInfo(request.POST or None)
    if form.is_valid():
        request.user.location = form.cleaned_data.get("location")
        request.user.degree = form.cleaned_data.get("degree")
        request.user.college = form.cleaned_data.get("college")
        request.user.year = form.cleaned_data.get("year")
        request.user.dob = form.cleaned_data.get("dob")
        request.user.activated = True
        request.user.save()
        return HttpResponseRedirect('/profile_page/')
    context = {"form":form}
    return render(request,'home/Extended_info.html',context)
