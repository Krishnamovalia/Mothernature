from django.contrib import admin
from .models import Customer,category,products,cart,gallery,order,payment,feedback
# Register your models here.

class displaycustomer(admin.ModelAdmin):
    list_display = ['user','name','email','address','city','contactno']
admin.site.register(Customer,displaycustomer)


class displaycategory(admin.ModelAdmin):
    list_display = ['categoryname','description']
admin.site.register(category,displaycategory)

class displayproduct(admin.ModelAdmin):
    list_display = ['admin_photo','categoryid','productname','productprice','productdes','image','qty']
admin.site.register(products,displayproduct)


class displaygallery(admin.ModelAdmin):
    list_display = ['admin_photo','image']
admin.site.register(gallery,displaygallery)

class displaycart(admin.ModelAdmin):
    list_display = ['qty','user','productid']
admin.site.register(cart,displaycart)


class displayorder(admin.ModelAdmin):
    list_display = ['qty','user','productid','cartid','customer','order_date','order_status']
admin.site.register(order,displayorder)

class displaypayment(admin.ModelAdmin):
    list_display = ['paymentstatus','paymentmode','amount','orderid']
admin.site.register(payment,displaypayment)


class displayfeedback(admin.ModelAdmin):
    list_display = ['feedbackdate','feedbackmsg','user','productid']
admin.site.register(feedback,displayfeedback)