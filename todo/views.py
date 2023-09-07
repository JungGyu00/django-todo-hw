from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request, 'todo/home.html')
    else:
        return HttpResponse('invalid request method', status='406')
