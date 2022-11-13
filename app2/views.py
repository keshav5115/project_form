from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from app2.models import usermodel
# Create your views here.
def create(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST.get('email')
        phone=request.POST['tel']
        usermodel.objects.create(name=name,email=email,phone=phone)

        messages.success(request, f'registration successfull {name}')
    return render(request,'index.html')

def update(request):
    
    if request.method=='POST':
        print(request.POST['value'])
        
        res=usermodel.objects.get(name=request.POST['value'])
        return render(request,'update1.html',{'res':res,'temp':True})
        # else:
        #     pk=request.POST['id']
        #     name=request.POST['username']
        #     email=request.POST.get('email')
        #     phone=request.POST['tel']
        #     usermodel.objects.filter(id=pk).update(name=name,email=email,phone=phone)
        #     return HttpResponse('data has been updated')

    res=usermodel.objects.all()
    return render(request,'update1.html',{'res':res,'temp':False})

def updaterecord(request):
    pk=request.POST['id']
    name=request.POST['username']
    email=request.POST.get('email')
    phone=request.POST['tel']
    usermodel.objects.filter(id=pk).update(name=name,email=email,phone=phone)
    return HttpResponse('data has been updated')