from django.contrib import admin
from .models import Stock, Supplier, Product, Category
# Register your models here.

admin.site.register(Stock)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Category)