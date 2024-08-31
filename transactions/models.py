import string, random
from django.db import models
from django.utils import timezone
from django.db.models import Sum
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from home.models import Stock

def generate_transaction_id():
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(12))

class SellItem(models.Model):
    id = models.CharField(max_length=8, primary_key=True, unique=True, default=generate_transaction_id, editable=False)
    stock_items = models.ManyToManyField(Stock, related_name='items_to_sell', blank=True)
    date_transaction = models.DateTimeField(default=timezone.now, editable=True)
    sold_to = models.CharField(max_length=255, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    @property   
    def TOTAL_PRICE(self):
        return self.stock_items.aggregate(total=Sum('product__selling_price'))['total'] or 0

    def save(self, *args, **kwargs):
        # Save SellItem instance first to ensure it exists in the database
        super().save(*args, **kwargs)

# Signal to calculate total price when stock_items are updated
@receiver(m2m_changed, sender=SellItem.stock_items.through)
def update_total_price(sender, instance, action, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        total_price = instance.stock_items.aggregate(total=Sum('product__selling_price'))['total'] or 0
        instance.total_price = total_price
        instance.save()
