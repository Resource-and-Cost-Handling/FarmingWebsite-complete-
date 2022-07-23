from pyexpat import model
from django.db import models
# from django import forms

# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length=122)
   email = models.CharField(max_length=122)
   phone = models.CharField(max_length=122)
   text = models.TextField()
   date = models.DateField()

def __str__(self):
    return self.name
 
# class Register(models.Model):
#    fname = models.CharField(max_length=122)
#    lname = models.CharField(max_length=122)
#    email = models.CharField(max_length=122)
#    number = models.CharField(max_length=12)
#    # password = models.CharField()
#    password = models.PROTECT()
#    date = models.DateField()
   
#    def __str__(self):
#       return self.fname
# class Register(forms.Form):
#    fname = models.CharField(max_length=122)
#    lname = models.CharField(max_length=122)
#    email = models.CharField(max_length=122)
#    number = models.CharField(max_length=12)
#    password=forms.CharFeild(widget=forms.PasswordInput)
#    rpassword=forms.CharFeild(widget=forms.PasswordInput)
#    def clean(self):
#       cleaned_data=super().clean()
#       valpwd=cleaned_data['password']
#       valpwd=cleaned_data['rpassword']
#       if valpwd!=valrpwd:
#          raise forms.ValidationError('Password not match')