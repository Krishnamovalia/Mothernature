from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import UserRegistrationForm
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm

urlpatterns = [
                  path('', views.index, name='index'),
                  path('product/<id>',views.Poduct,name='product'),
                  path('aboutus', views.aboutus, name='aboutus'),
                  path('contactus', views.contactus, name='contactus'),
                  path('faq', views.faq, name='faq'),
                  path('gallery', views.gallery, name='gallery'),
                  path('checkout1', views.checkout1, name='checkout1'),
                  path('addtocart', views.add_to_cart, name='addtocart'),
                  path('order', views.order, name='order'),
                  path('more', views.more, name='more'),
                  path('pdetails/<id>', views.pdetails, name='pdetails'),
                  path('profile', views.ProfileView.as_view(), name='profile'),
                  path('account/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm),
                       name='login'),

                  path('changepw', auth_views.PasswordChangeView.as_view(template_name='changepw.html',
                                                                         form_class=MyPasswordChangeForm,
                                                                         success_url='passwordchangedone'),
                                                                         name='changepw'),

                  path('passwordchangedone',
                       auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),
                                                                 name='passwordchangedone'),
                #password reset

                  path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
                  path('registration', views.UserRegistrationView.as_view(), name='registration'),
                  path('address', views.address, name='address'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
