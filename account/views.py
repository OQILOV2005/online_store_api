from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import User




@api_view(['POST'])
def signin_view(request):
   username = request.POST.get('username')
   password = request.POST.get('password')
   usr = authenticate(username=username, password=password)
   if usr is not None:
        login(request, usr)
   return Response({"message":"Log in"})


@api_view(["POST"])
def signup_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    User.objects.create_user(username=username, password=password)
    return Response({"message": "Register successful"})


def logout_view(request):
    logout(request)
    return Response("logout")

