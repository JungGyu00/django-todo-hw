from django.urls import path
from .views import signout, signup, signin

urlpatterns = [
    path('sign-up/', signup),
    path('sign-in/', signin),
    path('sign-out/', signout),
]
