import uuid
import random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.utils import timezone

def random_string(strings):
    return random.choice(strings)

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    product_name = models.CharField(max_length=255,default="Product 1",help_text="Official product name")
    description = models.TextField(help_text="Tell something about the product.")
    SKU = models.CharField(max_length=50, unique=True, help_text="SKU is a unique ID given mainly by manufacturers. Check the Unit or Documents if SKU is present.")
    category = models.OneToOneField(Category, related_name="products", on_delete=models.SET_NULL, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    expiry_date = models.DateField(default=timezone.now,null=True, blank=True, help_text="YYYY-MM-DD (Leave Blank if N/A)")
    notes = models.TextField(null=True, blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return self.product_name

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    supplier_code = models.CharField(max_length=50, unique=True, editable=False)

    def __str__(self):
        return self.name

class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock_name = models.CharField(max_length=255, default=random_string(["Gasul X","Wonder Gasul","Awesome Gasul","Gasul na Cool","Oh my Gas","Gas Gas Gas!"]))
    product = models.ForeignKey(Product, related_name="stocks", on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    date_received = models.DateField(default=timezone.now, editable=True,help_text="YYYY-MM-DD")
    date_last_ordered = models.DateField(null=True, blank=True, help_text="YYYY-MM-DD")
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('not_available','Not Available'), ('phased_out', 'Phased Out')])
    expiry_date = models.DateField(null=True, blank=True, help_text="YYYY-MM-DD (Expiry defaults with product category expiry)")
    
    def __str__(self):
        try:
            return f"{self.product.product_name}: {self.stock_name}"
        except AttributeError:
            return "N/A"

    def save(self, *args, **kwargs):
        if self.expiry_date is None and self.product:
            self.expiry_date = self.product.expiry_date
        super(Stock, self).save(*args, **kwargs)


# Signal to generate random supplier code before saving the model
@receiver(pre_save, sender=Supplier)
def generate_supplier_code(sender, instance, **kwargs):
    if not instance.supplier_code:
        instance.supplier_code = str(uuid.uuid4()).replace('-', '')[:8]

