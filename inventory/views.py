from django.shortcuts import render
from django.db.models import Count
from home.models import Stock, Category, Supplier, Product

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