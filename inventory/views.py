from django.shortcuts import render
from home.models import Stock, Category, Supplier, Product

# Create your views here.
def inventory_dashboard(request):
    var = {}
    var['inventory'] = Stock.objects.all()
    var['inventory_count'] = Stock.objects.count()
    return render(request, 'blocks/dashboard_components.html',var)  