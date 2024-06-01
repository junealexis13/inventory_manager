from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms

# Create your views here.
def landing_page(request):
    return render(request, "blocks/homepage_blocks.html", {})

def add_product(request):
    vars = {}
    vars["products"] = models.Stock.objects.all
    vars["product_number"] = models.Stock.objects.count()
    return render(request, "blocks/productpage_blocks.html",vars)

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
            return HttpResponseRedirect('/inventory_forms?submitted=True')

    else:
        if formID == "category":
            form = forms.CategoryForms
        elif formID == "supplier":
            form = forms.SupplierForms
        elif formID == "productSpecs":
            form = forms.ProductForms
        elif formID == "stocks":
            form = forms.StockForms
        else:
            form = None

        if "submitted" in request.GET:
            submitted = True    

    return render(request, "blocks/productpage_forms.html",{"formID": formID, "form": form, "submitted": submitted})

def login_page(request):
    return render(request, "home/login.html", {})

def dashboard(request):
    return render(request, "home/dashboard.html", {})
