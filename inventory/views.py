from django.shortcuts import render
from home.models import Stock, Category, Supplier, Product

# Create your views here.
def inventory_dashboard(request):
    var = {}


    return render(request, 'blocks/dashboard_components.html',var)  