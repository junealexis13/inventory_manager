from django import forms
from django.forms import ModelForm
from .models import Category, Product, Stock, Supplier

class CategoryForms(ModelForm):
    class Meta:
        model = Category
        fields = ["category"]

        labels = {
            "category" : "Specify Product Category"
        }
        widgets = {
            "category" : forms.TextInput(attrs={'class': 'form-control'})
        }

class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForms, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control','cols':'60'})

class StockForms(ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(StockForms, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control','cols':'60'})

class SupplierForms(ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SupplierForms, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control','cols':'60'})

class ProductDeleteForm(forms.Form):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

class CategoryDeleteForm(forms.Form):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

class SupplierDeleteForm(forms.Form):
    supplier = forms.ModelMultipleChoiceField(
        queryset=Supplier.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )