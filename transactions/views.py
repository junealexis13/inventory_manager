from django.shortcuts import render
from django.shortcuts import render, redirect
from transactions.forms import SellItemForm
from django.http import JsonResponse
from django.db.models import Sum
from django.views.decorators.http import require_POST
from home.models import Stock
from transactions.models import SellItem
# Create your views here.

@require_POST
def get_total_price(request):
    ids = request.POST.getlist('stock_items')
    total_price = Stock.objects.filter(id__in=ids).aggregate(total=Sum('product__selling_price'))['total'] or 0
    return JsonResponse({'total_price': total_price})

def transactions_dashboard(request):
    total_price = 0
    if request.method == 'POST':
        form = SellItemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SellItemForm()

    return render(request, 'blocks/transaction_components.html',
        {'form': form, 'total_price': total_price})