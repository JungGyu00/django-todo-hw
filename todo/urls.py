from django.urls import path
from .views import read, create

urlpatterns = [
    path('', read),
    path('create/', create),
]
