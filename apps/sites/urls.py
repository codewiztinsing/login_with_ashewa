
from django.contrib import admin
from django.urls import path
from .views import register_site,authenticate_site

urlpatterns = [
    path('', register_site,name="register_site"),
     path('<token>/', authenticate_site,name="authenticate_site"),
]
