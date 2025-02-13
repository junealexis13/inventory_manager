"""
URL configuration for inventory_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from home import views
from inventory import views as ivw
from transactions import views as tvw


urlpatterns = [
    path('', lambda request: redirect('mngr-home') if request.user.is_authenticated else redirect('login')),
    path('admin/', admin.site.urls, name="admin"),
    path('home', views.landing_page, name="mngr-home"),
    path('products/', views.add_product, name="mngr-products"),
    path('inventory_forms/', views.product_forms, name="mngr-forms"),
    path('login/', views.login_page, name="mngr-login"),
    path('edit_product/<int:pk>/', views.edit_product_specs, name='edit_product'),
    path('manage_entries', views.manage_entries, name='entry-mngr'),
    path('inventory/dashboard', ivw.inventory_dashboard, name='inventory-dashboard'),
    path('inventory/manage/edit/<item_id>', ivw.show_stock_data, name='inventory-item'),
    path('inventory/manage/remove',ivw.multi_remove_stocks, name='remove-stock-items'),
    path('transactions/dashboard', tvw.transactions_dashboard, name='transactions-dashboard'),
    path('get_total_price/', tvw.get_total_price, name='get_total_price'),
    path('authenticate/', include('django.contrib.auth.urls')),
    path('authenticate/', include('auth_app.urls')),
]
