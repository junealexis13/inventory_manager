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
        widgets = {
                    'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
                    'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the product'}),
                    'SKU': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter SKU'}),
                    'category': forms.Select(attrs={'class': 'form-control'}),
                    'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter weight in kg'}),
                    'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
                    'expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                    'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional notes (optional)'}),
                    'cost_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter cost price'}),
                    'selling_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter selling price'}),
                    'discount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter discount'}),
                }

class StockForms(ModelForm):
    class Meta:
        model = Stock
        exclude = ['is_sold']

        widgets = {
            'stock_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter stock name'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'date_received': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'date_last_ordered': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Optional'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Optional'}),
            'sold_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Optional'}),
        }


class SupplierForms(ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SupplierForms, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control','cols':'60'})

class DeleteForm(forms.Form):
    product_ids = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Product Entries', required=False)
    category_ids = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Category Entries', required=False)
    supplier_ids = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Supplier Entries', required=False)

    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        self.fields['product_ids'].choices = [(obj.id, str(obj)) for obj in Product.objects.all()]
        self.fields['category_ids'].choices = [(obj.id, str(obj)) for obj in Category.objects.all()]
        self.fields['supplier_ids'].choices = [(obj.id, str(obj)) for obj in Supplier.objects.all()]