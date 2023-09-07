from django.http import HttpResponse
from django.shortcuts import redirect, render
from todo.models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request, 'todo/home.html')
    else:
        return HttpResponse('invalid request method', status='406')


@login_required(login_url="/user/sign-in/")
@csrf_exempt
def create(request):
    if request.method == "POST":
        Todo.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            user=request.user,
        )

        return redirect('/todo/')

    elif request.method == "GET":
        return render(request, 'todo/create.html')
    else:
        return HttpResponse("invalid request mothod", status="405")


def read(request):
    todo_list = Todo.objects.all()
    return render(request, "todo/home.html", {"todo_list": todo_list})
