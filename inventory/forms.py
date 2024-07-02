from django import forms
from django.forms import ModelForm
from home.models import Category, Product, Stock, Supplier

class StockForms(ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(StockForms, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control','cols':'60'})
