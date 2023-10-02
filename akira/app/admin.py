from django.contrib import admin
from . models import Cart, Customer, Product, Payment, OrderPlaced
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
   list_display=['title', 'selling_price', 'discounted_price', 'category', 'product_image']
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
   list_display=['id', 'user', 'locality', 'city', 'state', 'zipcode']
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
   list_display = ['id', 'user', 'products', 'quantity']
   def products(self,obj):
      # link = reverse("admin:app_product_change",args=[obj.products.pk])
      link = reverse("admin:app_product_change", args=[obj.product.pk])
      return format_html('<a href="{}">{}</a>',link, obj.product.title)


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
   list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id', 'paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
   list_display = ['id', 'user', 'customers', 'products', 'quantity', 'ordered_date', 'status', 'payment']
   def customers(self,obj):
      link = reverse("admin:app_product_change", args=[obj.customer.pk])
      return format_html('<a href="{}">{}</a>',link, obj.customer.name)
   


   def products(self,obj):
      link = reverse("admin:app_product_change", args=[obj.product.pk])
      return format_html('<a href="{}">{}</a>',link, obj.product.title)
   

   
   


   


