from django.contrib import admin
from .models import Stock, Supplier, Pricing, Product, Category
# Register your models here.

admin.site.register(Stock)
admin.site.register(Supplier)
admin.site.register(Pricing)
admin.site.register(Product)
admin.site.register(Category)