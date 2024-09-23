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
    var['all'] = Stock.objects.all()
    var['for_sale'] = Stock.objects.filter(status='available').filter(is_sold=False)
    var['inventory_count'] = Stock.objects.count()

    var['not_sold'] = Stock.objects.filter(is_sold=False)
    var['sold'] = Stock.objects.filter(is_sold=True)
    var['not_sold_count'] = Stock.objects.filter(is_sold=False).count()
    var['sold_count'] = Stock.objects.filter(is_sold=True).count()

    var['status'] = {
        'available': Stock.objects.filter(status='available').count(),
        'not_available': Stock.objects.filter(status='not_available').count(),
        'phased_out': Stock.objects.filter(status='phased_out').count(),
    }

    itemCount_categorized = {}
    formID = request.GET.get('success', 'default')

    for cats in Category.objects.all():
        itemCount_categorized[cats.category] = 0

    for x in var['all']:
        if str(x) != 'N/A':
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

    return render(request, 'blocks/view_item_forms.html',var) 
    
def multi_remove_stocks(request):
    # pr_number = models.Product.objects.count()
    # cat_number = models.Category.objects.count()
    # sup_number = models.Supplier.objects.count()

    # if pr_number == 0 and cat_number == 0 and sup_number == 0:
    #     form_isEmpty= True 
    # else:
    #     form_isEmpty = False 


    if request.method == 'POST':
        form = forms.DeleteStockForm(request.POST)
        if form.is_valid():
            available_ids = form.cleaned_data['available_ids']
            not_available_ids = form.cleaned_data['not_available_ids']
            phased_out_ids = form.cleaned_data['phased_out_ids']

            Stock.objects.filter(id__in=available_ids).delete()
            Stock.objects.filter(id__in=not_available_ids).delete()
            Stock.objects.filter(id__in=phased_out_ids).delete()
            messages.success(request,"Successfully Removed Items")
            return HttpResponseRedirect('/inventory/dashboard')
        else:
            messages.error(request,f"An error occured: {form.errors}")
            return HttpResponseRedirect('/inventory/dashboard')
    else:
        form = forms.DeleteStockForm()


    return render(request, 'blocks/remove_stock_entries.html', {'form': form})