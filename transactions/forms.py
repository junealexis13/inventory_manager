from django import forms
from django.forms import ModelForm
from transactions.models import SellItem
from home.models import Stock

class Transact(ModelForm):
    class Meta:
        model = SellItem
        fields = ['sold_to', 'stock_items']
        widgets = {
            'selected_stocks': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock_items'].queryset = Stock.objects.all()
        self.fields['stock_items'].label_from_instance = lambda obj: f"{obj.product.product_name}: {obj.stock_name} | {str(obj.id)[:12]}..."