from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms

# Create your views here.
def landing_page(request):
    return render(request, "blocks/homepage_blocks.html", {})

def add_product(request):
    vars = {}
    vars["products"] = models.Product.objects.all()
    vars["product_number"] = models.Product.objects.count()
    vars["categories"] = models.Category.objects.all()
    vars["category_numbers"] = models.Category.objects.count()
    vars["suppliers"] = models.Supplier.objects.all()
    vars["supplier_numbers"] = models.Supplier.objects.count()
    return render(request, "blocks/productpage_blocks.html", vars)

def product_forms(request):
    formID = request.GET.get('formID', 'default')
    submitted = False
    if request.method == "POST":
        if formID == "category":
            form = forms.CategoryForms(request.POST)
        elif formID == "supplier":
            form = forms.SupplierForms(request.POST)
        elif formID == "productSpecs":
            form = forms.ProductForms(request.POST)
        elif formID == "stocks":
            form = forms.StockForms(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,"Form Successfully Updated")
            return HttpResponseRedirect('/products')
        else:
            messages.error(request,
                           f"An Error Occured: \n LOGS: {form.errors}")
            return HttpResponseRedirect('inventory_forms/?formID=productSpecs')


    else:
        if formID == "category":
            form = forms.CategoryForms()
        elif formID == "supplier":
            form = forms.SupplierForms()
        elif formID == "productSpecs":
            form = forms.ProductForms()
        elif formID == "stocks":
            form = forms.StockForms()
        else:
            form = None

        if "submitted" in request.GET:
            submitted = True    

    return render(request, "blocks/productpage_forms.html",{"formID": formID, "form": form, "submitted": submitted})

def login_page(request):
    return render(request, "home/login.html", {})

def dashboard(request):
    return render(request, "home/dashboard.html", {})


def edit_product_specs(request, pk):
    formID = request.GET.get('formID', 'default')
    submitted = False
    if request.method == 'POST':
        if formID == "productSpecs":
            object = get_object_or_404(models.Product, pk=pk)
            form = forms.ProductForms(request.POST, instance=object)
        elif formID == "category":
            object = get_object_or_404(models.Category, pk=pk)
            form = forms.CategoryForms(request.POST, instance=object)
        elif formID == "supplier":
            object = get_object_or_404(models.Supplier, pk=pk)
            form = forms.SupplierForms(request.POST, instance=object)

        if form.is_valid():
            form.save()
            messages.success(request,"Form Successfully Updated")
            return HttpResponseRedirect('/products/')
    else:

        if formID == "productSpecs":
            object = get_object_or_404(models.Product, pk=pk)
            form = forms.ProductForms(instance=object)
        elif formID == "category":
            object = get_object_or_404(models.Category, pk=pk)
            form = forms.CategoryForms(instance=object)
        elif formID == "supplier":
            object = get_object_or_404(models.Supplier, pk=pk)
            form = forms.SupplierForms(instance=object)

    return render(request, "blocks/productpage_forms.html", {"formID":formID,'form': form, "submitted": submitted})


def manage_entries(request):
    vars = {}
    pr_number = models.Product.objects.count()
    cat_number = models.Category.objects.count()
    sup_number = models.Supplier.objects.count()

    if pr_number == 0 and cat_number == 0 and sup_number == 0:
        vars['var_isEmpty'] = True 
    else:
        vars['var_isEmpty'] = False 

    if request.method == 'POST':
        form = forms.DeleteForm(request.POST)
        if form.is_valid():
            product_ids = form.cleaned_data['product_ids']
            category_ids = form.cleaned_data['category_ids']
            supplier_ids = form.cleaned_data['supplier_ids']

            models.Product.objects.filter(id__in=product_ids).delete()
            models.Category.objects.filter(id__in=category_ids).delete()
            models.Supplier.objects.filter(id__in=supplier_ids).delete()

            messages.success(request,"Successfully Deleted Items!")
            return HttpResponseRedirect('/inventory_forms')
        else:
            messages.error(request,
                           f"An Error Occured: \n LOGS: {form.errors}")
            return HttpResponseRedirect('/manage_entries')
    else:
        form = forms.DeleteForm()

    vars["form"] = form
    return render(request, "blocks/entry_mngr_blocks.html", vars)