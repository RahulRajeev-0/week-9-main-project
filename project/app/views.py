from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import User_details
# Create your views here.



#login page for users
def login(request):
    return render(request,'loginForUser.html')
        



#home page
def index(request):
    return render(request,'index.html')


# signup page
def signUp(request):
    data=User_details.objects.all()
    context={'data':data}
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('passwordConfirm')
        #print(name,email,password,confirm_password)
        if name and email and password and confirm_password:
            
            if password!=confirm_password:
                messages.warning(request,"Password is Incorrect")
                return redirect('/signUp')
            try:
                if User_details.objects.get(name=name):
                    messages.info(request,"Name Already Exist")
                    return redirect('/signUp')
            except:
                pass

            try:
                if User_details.objects.get(email=email):
                    messages.info(request,"Email Already Used ")
                    return redirect('/signUp')
            except:
                pass

        if password==confirm_password:
            query=User_details(name=name,email=email,password=password)
            query.save()
            messages.success(request,'data Registration successfully')
            return redirect('/index')
    
    return render(request,'signUp.html',context)


# admin login page 
def adminLog(request):
    return render(request,'loginForAdmin.html')