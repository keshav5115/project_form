from django import forms

from app1.models import studentmodel


class studentform(forms.Form):
    stu_id=forms.CharField()
    name=forms.CharField(widget=forms.TextInput)
    email=forms.EmailField(widget=forms.EmailInput)
    phone=forms.IntegerField()
    location=forms.CharField(widget=forms.TextInput)
