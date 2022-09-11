from rest_framework.generics import ListAPIView, RetrieveAPIView
from collections import OrderedDict
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer, CustomerSerializer, QuestionSerializer, \
    AddressSerializer, OrderSerializer, CategoryMealSerializer, ReviewSerializer
from ..models import Category, Product, Customer, Question, Address, Order, CategoryMeal, Review
from rest_framework.pagination import PageNumberPagination


class CategoryListAPI(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('objects_count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('items', data),
        ]))


class ProductListAPI(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    queryset = Product.objects.all()
    search_fields = ['price', 'name']


class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'


class CustomerListAPI(ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class QuestionListAPI(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class AddressListAPI(ListAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class OrderListAPI(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class CategoryMealListAPI(ListAPIView):
    serializer_class = CategoryMealSerializer
    queryset = CategoryMeal.objects.all()


class ReviewListAPI(ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
