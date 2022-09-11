from rest_framework import serializers
from ..models import Category, Product, Customer, Order, Question, CategoryMeal, Address, Review


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    category = serializers.CharField()
    # categorymeal = serializers.CharField()
    # description = serializers.CharField()
    # image = serializers.ImageField()
    price = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price']


class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = Customer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    topic = serializers.CharField()
    message = serializers.CharField()

    class Meta:
        model = Question
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    customer = serializers.CharField()
    order = serializers.CharField()
    phone = serializers.CharField()
    city = serializers.CharField()
    street = serializers.CharField()
    home_number = serializers.IntegerField()
    floor = serializers.IntegerField()
    door = serializers.IntegerField()

    class Meta:
        model = Address
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.CharField()
    date_ordered = serializers.DateTimeField()
    complete = serializers.BooleanField()
    transaction_id = serializers.CharField()

    class Meta:
        model = Order
        fields = '__all__'


class CategoryMealSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = CategoryMeal
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    text = serializers.CharField()
    email = serializers.EmailField()
    publish = serializers.DateTimeField()

    class Meta:
        model = Review
        fields = '__all__'
