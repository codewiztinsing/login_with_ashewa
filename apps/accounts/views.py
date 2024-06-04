from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.



def login_view(request):
    context = {}
    full_path = full_url_path = str(request.build_absolute_uri())
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        try:
            user = User.objects.filter(username = username)
            user = authenticate(request,username = username,password = password)
        
            if user is not None:
                login(request,user)
                return redirect("/")
        except User.DoesNotExist as e:
            raise e
       
    return render(request,"accounts/login.html",context)
