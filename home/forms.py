from django import forms
from djano.forms import ModelForm
from .models import Category, Product, Stock, Supplier

class CategoryForms(ModelForm):
    class Meta:
        model = Category
        fields = ["category"]


class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class StockForms(ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"

class SupplierForms(ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"