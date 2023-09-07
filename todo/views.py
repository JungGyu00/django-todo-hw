from django.http import HttpResponse
from django.shortcuts import redirect, render
from todo.models import Todo

# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request, 'todo/home.html')
    else:
        return HttpResponse('invalid request method', status='406')


def create(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "todo/create.html")
        elif request.method == "POST":
            Todo.objects.create(
                title=request.POST['title'], content=request.POST['content'], user=request.user)
            return redirect('/todo/')
        else:
            return HttpResponse('invalid request method', statud='405')
    else:
        return redirect('/user/sign-in')
