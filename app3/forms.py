from django import forms

from app3.models import studentmodel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import  make_password
class userform(UserCreationForm):
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=studentmodel
        fields=['username','first_name','last_name','email','phone','gender','password']
    def save(self,commit=True):
        user=super(userform,self).save(commit=False)
        user.password=make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user