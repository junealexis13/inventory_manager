from django.shortcuts import render

# Create your views here.

def transactions_dashboard(request):
    return render(request, 'blocks/transaction_components.html', {})