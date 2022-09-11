from django.urls import path
from .api_views import CategoryListAPI, ProductListAPI, CustomerListAPI, QuestionListAPI, AddressListAPI, \
    OrderListAPI, CategoryMealListAPI, ReviewListAPI,ProductDetailAPIView

urlpatterns = [
    path('categories/', CategoryListAPI.as_view(), name='category_list'),
    path('products/', ProductListAPI.as_view(), name='product_list'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('customers/', CustomerListAPI.as_view(), name='customer_list'),
    path('questions/', QuestionListAPI.as_view(), name='question_list'),
    path('address/', AddressListAPI.as_view(), name='address_list'),
    path('orders/', OrderListAPI.as_view(), name='order_list'),
    path('category_meals/', CategoryMealListAPI.as_view(), name='category_meal_list'),
    path('reviews/', ReviewListAPI.as_view(), name='review_list'),
]
