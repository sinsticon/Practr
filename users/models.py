from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from time import timezone
import datetime

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, name, phoneno):
        if not email:
            raise ValueError("No username entered")
        email = self.normalize_email(email)
        new_user = self.model(email=email,name=name, phoneno=phoneno)
        new_user.set_password(password)
        new_user.is_staff=False
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, email, password, name, phoneno):
        if not email:
            raise ValueError("No username entered")
        email = self.normalize_email(email)
        new_user = self.model(email=email,name=name, phoneno=phoneno)
        new_user.set_password(password)
        new_user.is_staff = True
        new_user.is_superuser = True
        new_user.save(using=self._db)
        return new_user



class student(AbstractBaseUser):
    email = models.EmailField(max_length=100,unique=True)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=200)
    phoneno=models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    experience = models.IntegerField(default=0)
    location = models.CharField(max_length=100,default='')
    degree = models.CharField(max_length=100,default='')
    activated = models.BooleanField(default=False)
    college = models.CharField(max_length=150,default='')
    year = models.CharField(max_length=10,choices=(('First','First'),
                                                   ('Second','Second'),
                                                   ('Third','Third')),
                            default='First')
    dob = models.DateField(default=datetime.date.today)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phoneno']
    objects=CustomUserManager()

    def get_absolute_url(self):
        return "/user/%s/" %self.email

    def get_name(self):
        return self.name
    def get_short_name(self):
        return self.name

    def get_phoneno(self):
        return self.phoneno

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def email_user(self,subject,message,from_mail=None):
        send_mail(subject,message,from_mail,[self.email])


class student_scores(models.Model):
    username=models.ForeignKey(student,on_delete=models.CASCADE)
    creativiy=models.IntegerField(default=0)
    presentation=models.IntegerField(default=0)
    overall=models.IntegerField(default=0)

class colleges(models.Model):
    college_name = models.CharField(max_length=150,default='')
    college_number = models.CharField(max_length=10)
    college_email = models.EmailField()


class clubs(models.Model):
    college_name = models.ForeignKey(colleges,on_delete=models.CASCADE,default='')
    club_name = models.CharField(max_length=100,default='')
