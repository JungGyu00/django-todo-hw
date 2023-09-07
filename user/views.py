from django.http import HttpResponse
from django.shortcuts import redirect, render
from user.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def signup(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['id'], password=request.POST['pw'])
        return redirect('/todo/')
    elif request.method == "GET":
        return render(request, "user/signup.html")
    else:
        return HttpResponse("invalid requset method", status="406")
