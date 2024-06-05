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

class DeleteForm(forms.Form):
    product_ids = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Product Entries', required=False)
    category_ids = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Category Entries', required=False)
    supplier_ids = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Supplier Entries', required=False)

    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        self.fields['product_ids'].choices = [(obj.id, str(obj)) for obj in Product.objects.all()]
        self.fields['category_ids'].choices = [(obj.id, str(obj)) for obj in Category.objects.all()]
        self.fields['supplier_ids'].choices = [(obj.id, str(obj)) for obj in Supplier.objects.all()]