from django import forms
from django.forms import ModelForm
from transactions.models import SellItem
from home.models import Stock

class SellItemForm(forms.ModelForm):
    class Meta:
        model = SellItem
        fields = ['sold_to', 'date_transaction', 'stock_items']
        widgets = {
            'sold_to': forms.TextInput(attrs={'class': 'form-control'}),
            'date_transaction': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stock_items': forms.SelectMultiple(attrs={'class': 'form-control select2-multiple'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock_items'].queryset = Stock.objects.filter(status='available')
        self.fields['stock_items'].label_from_instance = self.stock_label

    def stock_label(self, obj):
        return f"{obj.product.product_name}: {obj.stock_name} | {obj.id}"

    def clean_stock_items(self):
        stock_items = self.cleaned_data.get('stock_items')
        if not stock_items:
            raise forms.ValidationError("At least one stock item must be selected.")
        return stock_items
    
    def calculate_total_price(self):
        stock_items = self.cleaned_data.get('stock_items', [])
        return stock_items.aggregate(total=Sum('product__selling_price'))['total'] or 0
