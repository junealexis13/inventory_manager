from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def landing_page(request):
    return render(request, "blocks/homepage_blocks.html", {})

def add_product(request):

    vars = {}

    vars["products"] = models.Product.objects.all
    vars["product_number"] = models.Product.objects.count()

    return render(request, "blocks/productpage_blocks.html",vars)

def login_page(request):
    return render(request, "home/login.html", {})

def dashboard(request):
    return render(request, "home/dashboard.html", {})
