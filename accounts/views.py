from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import  User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from contact_details.models import Contact_detail
from hiretubers.models import Hiretuber

# Create your views here.
def login(request):
    contact_detail=Contact_detail.objects.all()
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Your logged in successfully')
            return redirect('dashboard')
        else:
            messages.warning(request,'Invalid Credentials') 
            return redirect('login')
    
    data={
        'contact_detail':contact_detail
    }
    

    return render(request,'accounts/login.html',data)

def register(request):
    contact_detail=Contact_detail.objects.all()
    if request.method == 'POST':
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        confirm_password= request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'Username exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,'email already exists')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,
                    email=email,password=password)
                    user.save()
                    messages.success(request,'Account created Successfully')
                    return redirect('login')
        else:
            messages.warning(request,'Password do not match')
            return redirect('register')
    data={
        'contact_detail':contact_detail
    }
        
    return render(request,'accounts/register.html',data)

def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    contact_detail=Contact_detail.objects.all()
    hiretuber=Hiretuber.objects.all()
    data={
        'contact_detail':contact_detail,
        'hiretuber':hiretuber
    }
    return render(request,'accounts/dashboard.html',data)