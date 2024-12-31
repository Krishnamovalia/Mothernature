from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,category,products,cart
from .forms import UserRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Sum

import json
# Create your views here.
def index(request):
    Category = category.objects.all()

    context = {
        'Category':Category,

    }
    return render(request,'index.html',context)

def Poduct(request,id):
    user = request.user
    if request.method == "GET":

        product_id = request.GET.get('product_id')

        if product_id is not None:
            print(product_id)
            product = products.objects.get(id=product_id)

            if cart.objects.filter(productid=product).exists():
                messages.success(request, 'This Product already added in cart')
                return redirect("addtocart")
            else:
                Cart = cart(
                    user=user,
                    productid=product,

                )
                Cart.save()
                messages.success(request, 'product are successfully added in cart')
                return redirect("addtocart")



    cat_details = category.objects.get(id=id)
    Category = category.objects.all()
    print(Category)
    prod = products.objects.filter(categoryid__id = id)

    context = {
        'prod':prod,
        'cat_details':cat_details,
        'Category':Category,
    }
    return render(request,'product.html',context)

def pdetails(request,id):
    Product = products.objects.get(id=id)
    Category = category.objects.all()
    context = {
        'Product': Product,
        'Category': Category,
    }

    return render(request, 'pdetails.html',context)


def aboutus(request):
    Category = category.objects.all()

    context = {
        'Category': Category,

    }
    return render(request, 'aboutus.html', context)

    return render(request,'aboutus.html')

def contactus(request):
    Category = category.objects.all()

    context = {
        'Category': Category,

    }
    return render(request, 'contactus.html', context)

    return render(request,'contactus.html')

def faq(request):
    Category = category.objects.all()

    context = {
        'Category': Category,

    }
    return render(request, 'faq.html', context)

    return render(request,'faq.html')

def gallery(request):
    Category = category.objects.all()

    context = {
        'Category': Category,

    }
    return render(request,'gallery.html',context)

def checkout1(request):
    Category = category.objects.all()

    context = {
        'Category': Category,

    }
    return render(request,'checkout1.html',context)

def add_to_cart(request):
    user = request.user
    delete_product = request.GET.get('delete_prod')
    if delete_product is not None:
        delete_prod = cart.objects.get(id = delete_product)
        delete_prod.delete()
        return redirect('addtocart')
    clear_cart = request.GET.get('clearcart')
    if clear_cart is not None:
       dCart = cart.objects.all()
       dCart.delete()
       return redirect('addtocart')
    Cart = None

    Cart = cart.objects.filter(user=user)
    total_amount = cart.objects.filter(user = request.user).aggregate(Sum('productid__productprice'))
    print(total_amount)
    Category = category.objects.all()

    context = {
        'Category': Category,
        'Cart':Cart,

    }
    return render(request, 'addtocart.html', context)

def order(request):
    Category = category.objects.all()

    context = {
        'Category': Category,

    }
    return render(request,'order.html',context)
'''
def profile(request):
    return render(request,'profile.html')
'''


class UserRegistrationView(View):
    def get(self, request):
       form = UserRegistrationForm()
       Category = category.objects.all()

       context = {
           'Category': Category,
           'form':form,

       }
       return render(request, 'registration.html',context)

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'You are successfully registered !')
            form.save()
        return render(request, 'registration.html',
         {'form': form})

def forgotpw(request):
    return render(request,'forgotpw.html')

def resetpw(request):
    return render(request,'resetpw.html')



def more(request):
    return render(request,'more.html')

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'profile.html',{'form':form,'active':'btn-success'})
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            contactno = form.cleaned_data['contactno']
            reg = Customer(user=usr,name=name,email=email,city=city,address=address,contactno=contactno)
            reg.save()
            messages.success(request,'congratulations!! profile updated successfully')
        return render(request,'profile.html',{'form':form,'active':'btn-success'})

def address(request):
    Category = category.objects.all()
    add = Customer.objects.filter(user = request.user)

    context = {
        'add':add,
        'active':'btn-success',
        'Category':Category,
    }
    return render(request, 'address.html',context)

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form}),