from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', updateItem, name='update_item'),
    path('add_order/', addOrder, name='add_order'),
    # path('accounts/signup/', addUser, name='account_signup'),
    path('accounts/signup/', signup, name='account_signup'),
    path('add_question/', addQuestion, name='add_question'),
]
