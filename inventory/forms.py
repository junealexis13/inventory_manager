from django import forms
from django.forms import ModelForm
from home.models import Stock

class StockForms(ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(StockForms, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control','cols':'60'})

class DeleteStockForm(forms.Form):
    available_ids = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Available Products', required=False)
    not_available_ids = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Unavailable Products', required=False)
    phased_out_ids = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Phased-out Products', required=False)

    def __init__(self, *args, **kwargs):
        super(DeleteStockForm, self).__init__(*args, **kwargs)
        self.fields['available_ids'].choices = [(obj.id, str(obj)) for obj in Stock.objects.filter(status='available')]
        self.fields['not_available_ids'].choices = [(obj.id, str(obj)) for obj in Stock.objects.filter(status='not_available')]
        self.fields['phased_out_ids'].choices = [(obj.id, str(obj)) for obj in Stock.objects.filter(status='phased_out')]
