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


from plotly.offline import plot
import plotly.express as px
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

def modify_update_layout(fig, color='RebeccaPurple'):
    fig.update_layout(
        title_font=dict(size=24, family='Arial', color='black'),
        xaxis_title="",
        yaxis_title="Revenue",
        xaxis=dict(tickangle=-90),
        font=dict(family="Courier New, monospace", size=10, color=color)
    )

    fig.update_layout(
        height=400
    )

    fig.update_traces(marker_color=color)


def transactions_dashboard(request):
    total_price = 0
    transactions = SellItem.objects.all()
    tx_count = transactions.count()

    now = timezone.now()
    year_now = datetime.now().year
    day_ago = now - timedelta(days=1)

    if tx_count != 0:
        day_revenue = [
                    {
                        'price': x.total_price,
                        'date_transaction': x.date_transaction
                    } for x in transactions if day_ago <= x.date_transaction <= now
                ]


        all_revenue = [
            {
                'price': x.total_price,
                'date_transaction': x.date_transaction
            } for x in transactions
        ]

        quarter_revenue = [
            {
                'price': sum([float(x.total_price) for x in transactions 
                            if x.date_transaction >= timezone.make_aware(datetime(year_now, 1, 1)) 
                            and x.date_transaction <= timezone.make_aware(datetime(year_now, 3, 31))]),
                'quarter': 'First Quarter'
            },
            {
                'price': sum([float(x.total_price) for x in transactions 
                            if x.date_transaction >= timezone.make_aware(datetime(year_now, 4, 1)) 
                            and x.date_transaction <= timezone.make_aware(datetime(year_now, 6, 30))]),
                'quarter': 'Second Quarter'
            },
            {
                'price': sum([float(x.total_price) for x in transactions 
                            if x.date_transaction >= timezone.make_aware(datetime(year_now, 7, 1)) 
                            and x.date_transaction <= timezone.make_aware(datetime(year_now, 9, 30))]),
                'quarter': 'Third Quarter'
            },
            {
                'price': sum([float(x.total_price) for x in transactions 
                            if x.date_transaction >= timezone.make_aware(datetime(year_now, 10, 1)) 
                            and x.date_transaction <= timezone.make_aware(datetime(year_now, 12, 31))]),
                'quarter': 'Fourth Quarter'
            }
        ]


        df1 = pd.DataFrame(all_revenue)
        df2 = pd.DataFrame(day_revenue)
        df3 = pd.DataFrame(quarter_revenue)
        fig1 = px.bar(df1, x='date_transaction', y='price',title='All-Time Revenue')
        modify_update_layout(fig1, color='navy')
        fig2 = px.bar(df2, x='date_transaction', y='price',title='Daily Revenue')
        modify_update_layout(fig2, color='teal')
        fig3 = px.bar(df3, x='quarter', y='price',title=f'Quarterly Revenue: {str(year_now)} ')
        modify_update_layout(fig3, color='maroon')
        sold_data_all = plot(fig1, output_type="div")
        sold_data_daily = plot(fig2, output_type="div")
        sold_data_quarterly = plot(fig3, output_type="div")

        print(quarter_revenue)


    else:
        sold_data_all, sold_data_daily,sold_data_quarterly= None

    if request.method == 'POST':
        form = SellItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Transaction Records updated!")
            return redirect('/transactions/dashboard?success=True')
    else:
        form = SellItemForm()

    return render(request, 'blocks/transaction_components.html',
        {'form': form, 'total_price': total_price, 'transactions': transactions, 
        'transaction_count': tx_count, 
        "plotly_sold_all": sold_data_all,
        "plotly_sold_daily": sold_data_daily,
        "plotly_sold_quarterly": sold_data_quarterly})