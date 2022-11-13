from django.shortcuts import render,redirect
from django.http import HttpResponse
from app3.forms import userform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def userview(request):
    form=userform()
    if request.method=='POST':
        form=userform(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponse('register')
    return render(request,'reg.html',{'form':form})


def loginview(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/app3/homepage/")
            else:
                messages.error(request, "Invalid username or password.")
                # messages= messages.get_messages(request)
        else:
            messages.error(request, "Invalid username or password.")
            # messages= messages.get_messages(request)
    return render(request,'login.html',{'form':form})

@login_required(login_url='/app3/login/')
def homepage(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    messages.success(request,"logout successfully")
    # messages= messages.get_messages(request)
    return redirect('/app3/reg/')