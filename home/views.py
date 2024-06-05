from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
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
            return HttpResponseRedirect('/inventory_forms?submitted=True')

    else:
        if formID == "category":
            form = forms.CategoryForms
            productObj = None
            catObj = None
            suppObj = None

        elif formID == "supplier":
            form = forms.SupplierForms
            productObj = None
            catObj = None
            suppObj = None

        elif formID == "productSpecs":
            form = forms.ProductForms
            productObj = None
            catObj = None
            suppObj = None

        elif formID == "stocks":
            form = forms.StockForms
            productObj = None
            catObj = None
            suppObj = None

        elif formID == "removeItems":
            form = None
            productObj = forms.ProductDeleteForm(request.POST)
            catObj = forms.CategoryDeleteForm(request.POST)
            suppObj = forms.SupplierDeleteForm(request.POST)

            form_logic = (productObj.is_valid(), catObj.is_valid(), suppObj.is_valid())

            match form_logic:
                case (True, True, True):
                    products_to_delete = productObj.cleaned_data['products']
                    category_to_delete = catObj.cleaned_data['category']
                    supplier_to_delete = suppObj.cleaned_data['supplier']
                    products_to_delete.delete()
                    category_to_delete.delete()
                    supplier_to_delete.delete()
                    return HttpResponseRedirect('/products/')

                case (True, True, False):
                    products_to_delete = productObj.cleaned_data['products']
                    category_to_delete = catObj.cleaned_data['category']
                    products_to_delete.delete()
                    category_to_delete.delete()
                    return HttpResponseRedirect('/products/')

                case (False ,True ,True):
                    category_to_delete = catObj.cleaned_data['category']
                    supplier_to_delete = suppObj.cleaned_data['supplier']
                    category_to_delete.delete()
                    supplier_to_delete.delete()
                    return HttpResponseRedirect('/products/')

                case (True, False, True):
                    products_to_delete = catObj.cleaned_data['category']
                    supplier_to_delete = suppObj.cleaned_data['supplier']
                    products_to_delete.delete()
                    supplier_to_delete.delete()
                    return HttpResponseRedirect('/products/')

                case (True, False, False):
                    products_to_delete = productObj.cleaned_data['products']
                    products_to_delete.delete()
                    return HttpResponseRedirect('/products/')

                case (False, True, False):
                    category_to_delete = productObj.cleaned_data['products']
                    category_to_delete.delete()
                    return HttpResponseRedirect('/products/')

                case (False, False, True):
                    products_to_delete = productObj.cleaned_data['products']
                    products_to_delete.delete()
                    return HttpResponseRedirect('/products/')

        else:
            form = None
            productObj = None
            catObj = None
            suppObj = None

        if "submitted" in request.GET:
            submitted = True    

    return render(request, "blocks/productpage_forms.html",{"formID": formID, "form": form, "submitted": submitted,
        "prodsObj":productObj,"catObj":catObj,"suppObj":suppObj})

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
            return HttpResponseRedirect('/inventory_forms?submitted=True')
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