from django.shortcuts import render, redirect
from django.dispatch import receiver
from django.contrib import messages
from django.db.models.signals import post_save
from transactions.forms import SellItemForm
from django.http import JsonResponse
from django.db.models import Sum
from django.views.decorators.http import require_POST
from home.models import Stock
from transactions.models import SellItem

@require_POST
def get_total_price(request):
    ids = request.POST.getlist('stock_items')
    total_price = Stock.objects.filter(id__in=ids).aggregate(total=Sum('product__selling_price'))['total'] or 0
    return JsonResponse({'total_price': total_price})

@receiver(post_save, sender=SellItem)
def update_stock_is_sold(sender, instance, **kwargs):
    #update is_sold status for all related/ selected items stock items
    instance.stock_items.update(is_sold=True)

def transactions_dashboard(request):
    total_price = 0
    transactions = SellItem.objects.all()
    if request.method == 'POST':
        form = SellItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Transaction Records updated!")
            return redirect('/transactions/dashboard?success=True')
    else:
        form = SellItemForm()

    return render(request, 'blocks/transaction_components.html',
        {'form': form, 'total_price': total_price, 'transactions': transactions})