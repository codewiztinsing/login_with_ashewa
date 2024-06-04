from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
from .models import Site
import uuid
# Create your views here.



def register_site(request):
    token = uuid.uuid1()
    context = {}
    
    if request.method == "POST":
        print("data=",request.POST)
        site_name    = request.POST.get("site_name")
        base_url = request.POST.get("base_url")
        redirect_url = f"https://{base_url}/{token}/"
        Site.objects.create(site_name = site_name,base_url = base_url,redirect_url = redirect_url)
    return render(request,"sites/site.html",context)


@login_required
def authenticate_site(request,token):
    _token = f"{token}"
    path = request.path
    user = request.user
    try:
        site = Site.objects.filter(token = _token).first()
        
    except Site.DoesNotExist as e:
        raise e
    
    if site:
        data = {
            "id":user.id,
            "username":user.username,
            "email":user.email,
            "is_active":user.is_active,
            "is_superuser":user.is_superuser,
                    
        }
        requests.post(site.base_url,data=data)
        return JsonResponse(data)
    else:
        return JsonResponse({
            'message':"site not found"
        })
