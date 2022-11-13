from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import studentmodel

from app1.forms import studentform
# Create your views here.
def studentview(request):
    form=studentform()
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            stu_id=request.POST['stu_id']
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            loc=request.POST['location']
            p=studentmodel.objects.create(stu_id=stu_id,name=name,email=email,phone=phone,location=loc)
        return redirect('/app1/read/')
    return render(request,'student.html', {'form':form})

def read(request):
    data=studentmodel.objects.all().values()
    

    return render(request,'read.html',{'data':data})
def update(request):
    if request.method=='POST':
        sid= request.POST['sid']
        res=studentmodel.objects.filter(stu_id=sid)
        return render(request,'update.html',{'res':res})
    return render(request,'update.html')

def update_value(request,sid):
    if request.method=="POST":
        name =request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        location=request.POST['location']
        print(name,email,phone,location)
        res=studentmodel.objects.filter(stu_id=sid).update(name=name,email=email,phone=phone,location=location)
        #return HttpResponse('update')
        return redirect('/app1/register/')
    return render(request,'insert.html')