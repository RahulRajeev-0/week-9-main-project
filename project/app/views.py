from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login as login_auth,logout
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from app.forms import User_form

# Create your views here.



#login page for users
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if 'session_user' in request.session:
        return redirect('/index')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        myuser = authenticate(username=username, password=password)
        print(myuser)
        if myuser is not None:
            request.session['session_user']=username
            login_auth(request, myuser)
            #return render(request,'loginForUser.html',context)
            messages.success(request,'Loged In successfully')
            return redirect('/index')
        else:
            messages.warning(request,"invalid Credential")
            return redirect('/')
    

    context={}
    
    return render(request,'loginForUser.html',context)
    
        



#home page
def index(request):
    if 'session_user' in request.session:
        return render(request,'index.html')
    return redirect('/')




# signup page for the user
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signUp(request):
    if 'session_user' in request.session:
        return redirect('/index')
    data=User.objects.all()
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
                if User.objects.get(username=name):
                    messages.info(request,"Name Already Exist")
                    return redirect('/signUp')
            except:
                pass

            try:
                if User.objects.get(email=email):
                    messages.info(request,"Email Already Used ")
                    return redirect('/signUp')
            except:
                pass

        if password==confirm_password:
            query=User.objects.create_user(name,email,password)
            query.save()
            request.session['session_user']=name
            messages.success(request,'Registration successfully')
            return redirect('/index')
    
    return render(request,'signUp.html',context)



#logout function for user
def logout_user(request):
    if 'session_user' in request.session:
        request.session.flush()
        logout(request)
        messages.info(request,'Loged Out')
        return redirect("/signUp")




# admin login page 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminLog(request):
    #if 'session_aduser' in request.session:
    #    return redirect('/admin_index')
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('/admin_index')
    
    if request.method=='POST':
        adname=request.POST.get('username')
        adpassword=request.POST.get('password')
        print(adname,adpassword)
        user=authenticate(username=adname,password=adpassword)
        print(user)
        if user is not None and user.is_superuser:
            login_auth(request,user)
        #    request.session['session_aduser']=adname
            messages.success(request,'LogIn successfully')
            return redirect ('/admin_index')
        else:
            messages.warning(request,"invalid credentials")
            return redirect('/adminLog')
    return render(request,'loginForAdmin.html')





#fucntion for rendering the index or the admin panel html page
def admin_index(request):
    if request.user.is_authenticated and request.user.is_superuser:
        users=User.objects.all()
        context={'users':users}
        return render(request,'Admin_CRUD_page.html',context)
    return redirect('/adminLog')






#function for the admin to create a user
def ad_create_user(request):

        
    data=User.objects.all()
    context={'data':data}
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('passwordConfirm')
        print(name,email,password,confirm_password)
        if name and email and password and confirm_password:
            
            if password!=confirm_password:
                messages.warning(request,"Password is Incorrect")
                return redirect('/ad_create_user')
            try:
                if User.objects.get(username=name):
                    messages.info(request,"Name Already Exist")
                    return redirect('/ad_create_user')
            except:
                pass

            try:
                if User.objects.get(email=email):
                    messages.info(request,"Email Already Used ")
                    return redirect('/ad_create_user')
            except:
                 pass

            if password==confirm_password:
                query=User.objects.create_user(name,email,password)
                query.save()
                messages.success(request,'Registration successfully')
    return render(request,'ad_create_user.html')  
    

 



#function for admin to edit the user details 
def ad_edit(request,id):
   
    user=User.objects.get(id=id)
    form=User_form(instance=user)
    if request.method=='POST':
        form = User_form(request.POST, instance=user)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect('admin_index')
        else:
            messages.error(request,form.errors)
            context={'form':form}
            return render(request,'ad_edit.html',context)
            
    context={'form':form}
    return render(request,'ad_edit.html',context)



# function for deleting the user
def ad_delete_user(request,id):
    user=User.objects.get(id=id)
    user.delete()
    messages.warning(request,'Deleted')
    return redirect('/admin_index')

#function for logout in admin index panel 
def logout_admin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        logout(request)
        messages.info(request,'Loged Out')
        return redirect('/adminLog')


