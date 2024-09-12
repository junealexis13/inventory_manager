from django.shortcuts import render, redirect
from django.utils import timezone
from django.dispatch import receiver
from django.contrib import messages
from django.db.models.signals import post_save
from transactions.forms import SellItemForm
from django.http import JsonResponse
from django.db.models import Sum
from django.views.decorators.http import require_POST
from home.models import Stock
from transactions.models import SellItem

from transactions.plot_data import PLOT_DATA
import pandas as pd 
from datetime import datetime, timedelta

@require_POST
def get_total_price(request):
    ids = request.POST.getlist('stock_items')
    total_price = Stock.objects.filter(id__in=ids).aggregate(total=Sum('product__selling_price'))['total'] or 0
    return JsonResponse({'total_price': total_price})

@receiver(post_save, sender=SellItem)
def update_stock_is_sold(sender, instance, **kwargs):
    #update is_sold status for all related/ selected items stock items
    instance.stock_items.update(is_sold=True)
    instance.stock_items.update(status='not_available')

def modify_update_layout(fig, color='RebeccaPurple', ttype=None):
    fig.update_layout(
        title_font=dict(size=24, family='Arial', color='black'),
        xaxis_title="",
        yaxis_title="Revenue",
        xaxis=dict(tickangle=-90),
        font=dict(family="Courier New, monospace", size=10, color=color),
        bargap=0.1
    )

    fig.update_layout(
        height=400
    )

    fig.update_traces(marker_color=color)

    if ttype == 'all':
        fig.update_xaxes(
                dtick=43200000*2, 
                tickformat="%b %d" 
            )


def transactions_dashboard(request):
    total_price = 0
    transactions = SellItem.objects.all()
    tx_count = transactions.count()

    Figures = PLOT_DATA(tx_count=tx_count, transaction_objects=transactions)
    sold_data_daily, sold_data_all, sold_data_quarterly = Figures.get_figs(datatype='revenue')
    profit_data_daily, profit_data_all, profit_data_quarterly = Figures.get_figs(datatype='profit')
    if request.method == 'POST':
        form = SellItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Transaction Records updated!")
            return redirect('/transactions/dashboard?success=True')
        else:
            messages.error(request,f"An error occured: {form.errors}")
            return redirect('/transactions/dashboard')
    else:
        form = SellItemForm()

    return render(request, 'blocks/transaction_components.html',
        {'form': form, 'total_price': total_price, 'transactions': transactions, 
        'transaction_count': tx_count, 
        "plotly_sold_all": sold_data_all,
        "plotly_sold_daily": sold_data_daily,
        "plotly_sold_quarterly": sold_data_quarterly,
        "plotly_profit_all": profit_data_all,
        "plotly_profit_daily": profit_data_daily,
        "plotly_profit_quarterly": profit_data_quarterly,})