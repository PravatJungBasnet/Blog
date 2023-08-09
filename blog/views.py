from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import signup,Postform
from django.contrib.auth import login,logout,authenticate
from .models import post


# Create your views here.
def home(request):
    posts=post.objects.all()
    return render(request,'blog/home.html',{'pt':posts})
def about(request):
    return render(request,'blog/about.html')
def contact(request):
    return render(request,'blog/contact.html')
# signup
def user_sign(request):
    if request.method=='POST':
        fm=signup(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/log/')
    else:
        fm=signup()
    return render(request,'blog/sign.html',{'form':fm})
#login
def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/das/') 
    else:
        fm=AuthenticationForm()
    return render(request,'blog/login.html',{'form':fm})  
   
def dashboard(request):
    if request.user.is_authenticated:
        posts=post.objects.all()
   
        return render(request,'blog/dashboard.html',{'pt':posts})
    else:
        return HttpResponseRedirect('/log/')


#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/log/')
def delete_post(request,id):
    if request.method=='POST':
        dl=post(pk=id)
        dl.delete()
        return HttpResponseRedirect('/das/')

def add_post(request):
    if request.method=='POST':
        fm=Postform(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/das/')
    else:
        fm=Postform()
    return render(request,'blog/addpost.html',{'form':fm})
def update(request,id):
    if request.method=='POST':
        pi=post.objects.get(pk=id)
        fm=Postform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/das/')
    else:
        pi=post.objects.get(pk=id)
        fm=Postform(instance=pi)
    return render(request,'blog/update.html',{'form':fm})
    
    
            


