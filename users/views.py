from django.shortcuts import render
from . models import student
from .forms import RegisterModel
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    form = RegisterModel(request.POST or None)
    created=False
    if form.is_valid():
        new_user = form.save(commit=False)
        username=form.cleaned_data['username']
        new_user_test,created = student.objects.get_or_create(username=username)
        if created:
            new_user.save()
            return HttpResponseRedirect('/user/')   #pass pk at the user/'pk'
    context={"form":form, "created":created}
    return render(request,'home/index.html',context)


def user_page(request):
    return HttpResponse("<h1>In user details page </h1>")