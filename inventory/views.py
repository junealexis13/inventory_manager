from django.shortcuts import render
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.contrib import messages
from home.models import Stock, Category, Supplier, Product
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms

# Create your views here.
def inventory_dashboard(request):
    var = {}
    var['inventory'] = Stock.objects.all()
    var['inventory_count'] = Stock.objects.count()

    itemCount_categorized = {}
    formID = request.GET.get('success', 'default')

    for cats in Category.objects.all():
        itemCount_categorized[cats.category] = 0

    for x in var['inventory']:
        str_x = str(x.product.category)
        itemCount_categorized[str_x] += 1
        
    var['item_count'] = dict(sorted(itemCount_categorized.items(), key=lambda item: item[1], reverse=True))

    
    return render(request, 'blocks/dashboard_components.html',var)  


def show_stock_data(request, item_id):
    var = {}
    submitted = False
    formID = request.GET.get('formID', 'default')
    item = get_object_or_404(Stock, pk=item_id)

    if request.method == "POST":
        form = forms.StockForms(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,"Inventory Successfully Updated")
            return HttpResponseRedirect('/inventory/dashboard?success=True')

    else:
        form = forms.StockForms(instance=item)
        if "submitted" in request.GET:
            submitted = True

    var['formID'] = formID
    var['form'] = form
    var['submitted'] = submitted   
    var['item'] = item
    

    return render(request, 'blocks/view_item_forms.html', var)