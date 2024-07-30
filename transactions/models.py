import string, random
from django.db import models
from django.utils import timezone
from django.db.models import Sum
from home.models import Product, Supplier, Stock, Category
# Create your models here.

def generate_transaction_id():
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(12))

class SellItem(models.Model):
    id = models.CharField(max_length=8, primary_key=True, unique=True, default=generate_transaction_id, editable=False)
    stock_items = models.ManyToManyField(Stock, related_name='items_to_sell', null=True)
    date_transaction = models.DateField(default=timezone.now, editable=True)
    sold_to = models.CharField(max_length=255, blank=True, null=True)

    @property
    def TOTAL_PRICE(self):
        return self.stock_items.aggregate(total=Sum('product__selling_price'))['total'] or 0
