from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from blogg.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'home/home.html')
def about(request):
    return render(request,'home/about.html')
def contact(request):
    
    if request.method=='POST':
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        query=request.POST["content"]
        print(name,email,phone,query)
        if len(name)<2 or len(email)<10 or len(phone)<10 or len(query)<5:
            messages.error(request,"PLease fill the details correctly!!")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=query)
            contact.save()
            messages.success(request,"Your query has been succesfully sent!!")
    return render(request,'home/contact.html')
def search(request):
    query=request.GET["search"]
    allPosts=Post.objects.filter(title__icontains=query)
    context={
        'posts':allPosts,
        'search':query,
    }
    return render(request,'home/search.html',context)
def handleLogIn(request):
    if request.method=='POST':
        loginusername=request.POST["loginusername"]
        loginpassword=request.POST["pass"]
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Succesfully logged in")
            return redirect("home")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('home')
    else:
        return HttpResponse("404-Not Found")
def handleLogOut(request):
    logout(request)
    messages.success(request,"Succesfully logged out")
    return redirect("home")
def handleSignUp(request):
    if request.method=='POST':
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        if len(username)>20:
            messages.error(request,"Username should not exceed 20 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('home')
        if pass1!=pass2:
            messages.error(request,"Confirm password must be the same as password")
            return redirect('home')
        myUser=User.objects.create_user(username,email,pass1)
        myUser.first_name=fname
        myUser.last_name=lname
        myUser.save()
        messages.success(request,"Your CodeVerse account is created successfully")
        return redirect('home')
    else:
        return HttpResponse("404-Not Found")

