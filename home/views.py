from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing_page(request):
    return render(request, "home/homepage.html", {})

def login_page(request):
    return render(request, "home/login.html", {})

def dashboard(request):
    return render(request, "home/dashboard.html", {})