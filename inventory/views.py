from django.shortcuts import render
from django.db.models import Count
from home.models import Stock, Category, Supplier, Product
from . import models, forms

# Create your views here.
def inventory_dashboard(request):
    var = {}
    var['inventory'] = Stock.objects.all()
    var['inventory_count'] = Stock.objects.count()

    itemCount_categorized = {}

    for cats in Category.objects.all():
        itemCount_categorized[cats.category] = 0

    for x in var['inventory']:
        str_x = str(x.product.category)
        itemCount_categorized[str_x] += 1
        
    var['item_count'] = itemCount_categorized
    return render(request, 'blocks/dashboard_components.html',var)  


def show_stock_data(request, item_id):
    var = {}
    item = Stock.objects.get(pk=item_id)
    form = forms.StockForms

    var['forms'] = form
    var['form'] = form
    return render(request, 'chunks/stocks_forms.html', var)