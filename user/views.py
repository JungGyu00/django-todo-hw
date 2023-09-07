from django.http import HttpResponse
from django.shortcuts import redirect, render
from user.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def signup(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['id'], password=request.POST['pw'])
        return redirect('/todo/')
    elif request.method == "GET":
        return render(request, "user/signup.html")
    else:
        return HttpResponse("invalid requset method", status="406")


def signin(request):
    if request.method == "POST":
        username = request.POST['id']
        password = request.POST['pw']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/todo/")
        else:
            return redirect("/user/sign-in/")
    elif request.method == "GET":
        return render(request, 'user/signin.html')
    else:
        return HttpResponse("invalid requset method", status="406")


def signout(request):
    logout(request)
    return redirect('/todo/')
