from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    contactno = models.BigIntegerField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)


class category(models.Model):
    categoryname=models.CharField(max_length=15)
    description=models.TextField(max_length=250)

    def __str__(self):
        return self.categoryname


class products(models.Model):
    categoryid = models.ForeignKey(category, on_delete=models.CASCADE)
    productname = models.CharField(max_length=70)
    productprice = models.IntegerField()
    productdes = models.CharField(max_length=500)
    image = models.ImageField(upload_to='photos')
    qty = models.IntegerField()

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))

    def __str__(self):
        return self.productname
    admin_photo.allow_tags = True

class gallery(models.Model):
    image=models.ImageField(upload_to='photos')

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))


    admin_photo.allow_tags = True

class cart(models.Model):
    qty=models.PositiveIntegerField(default =1)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='',null=False)
    productid=models.ForeignKey(products,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)
class order(models.Model):
    qty=models.PositiveIntegerField(default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='',null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,default='',null=False)
    productid =models.ForeignKey(products,on_delete=models.CASCADE)
    cartid=models.ForeignKey(cart,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

class payment(models.Model):
    paymentstatus=models.CharField(max_length=10)
    paymentmode=models.CharField(max_length=15)
    amount=models.IntegerField()
    orderid=models.ForeignKey(order,on_delete=models.CASCADE)



class feedback(models.Model):
    feedbackdate=models.DateTimeField(auto_now=True, editable=False)
    feedbackmsg=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='',null=False)
    productid=models.ForeignKey(products,on_delete=models.CASCADE)


