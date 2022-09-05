from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=200, null=True)
    email = models.CharField('Почта', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customers'
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Category(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        db_table = 'category'
        verbose_name = "Категория"
        verbose_name_plural = "Категория"

    def __str__(self):
        return self.name


class CategoryMeal(models.Model):
    name = models.CharField('Название(Трапеза)', max_length=255)

    class Meta:
        db_table = 'categorymeals'
        verbose_name = "Трапеза"
        verbose_name_plural = "Трапеза"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Имя', max_length=150)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    categorymeal = models.ForeignKey(CategoryMeal, verbose_name='Трапеза', on_delete=models.CASCADE)
    description = models.TextField('Описание', max_length=1000)
    image = models.ImageField('Изображение', upload_to='products/')
    price = models.IntegerField('Цена')

    class Meta:
        db_table = 'products'
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_cart_total(self):
        # print(self.cart_set.all())
        # print(self.orderitem)
        cart = self.orderitem_set.all()
        total = sum([item.get_total for item in cart])
        return total

    @property
    def get_cart_items(self):
        cart = self.orderitem_set.all()
        total = sum([item.quantity for item in cart])
        return total

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = 'orders'
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField('Количество', default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    class Meta:
        db_table = 'orderitems'
        verbose_name = "Позиции заказа"
        verbose_name_plural = "Позиции заказы"

    def __str__(self):
        return f"{self.order.customer} - {self.product.name} - {self.quantity}"


class Cart(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField('Количество', default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"{self.order.customer} - {self.product.name} - {self.quantity}"


class Question(models.Model):
    name = models.CharField('Имя', max_length=150)
    email = models.EmailField('Email')
    topic = models.CharField('Тема', max_length=300, blank=True, null=True)
    message = models.TextField('Сообщение', max_length=5000)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        db_table = 'questions'
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

class Address(models.Model):
    CITY = [
        ('ALA', 'Алматы'),
        ('NQZ', 'Нур-Султан'),
        ('CIT', 'Шымкент'),
    ]
    customer = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField('Телефон №', max_length=20)
    city = models.CharField('Город', choices=CITY, default='ALA', max_length=15)
    street = models.CharField('Улица', max_length=30)
    home_number = models.IntegerField('Дом №')
    floor = models.IntegerField('Этаж №')
    door = models.IntegerField('Квартира №')

    def __str__(self):
        return f"Адресс №{self.order} заказа"

    class Meta:
        db_table = 'address'
        verbose_name = "Адрес"
        verbose_name_plural = "Адресы"


class Review(models.Model):
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    email = models.EmailField()
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        db_table = 'reviews'
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
