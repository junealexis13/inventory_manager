from django.shortcuts import render
from django.shortcuts import render, redirect
from transactions.forms import Transact
from transactions.models import SellItem
# Create your views here.

def transactions_dashboard(request):
    if request.method == 'POST':
            form = Transact(request.POST)
            if form.is_valid():
                new_model = form.save()
    else:
        form = Transact()
        

    return render(request, 'blocks/transaction_components.html', {'form': form})