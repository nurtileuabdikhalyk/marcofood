from django.contrib import admin
from .models import *

admin.site.register(Address)
admin.site.register(OrderItem)
admin.site.register(Question)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(CategoryMeal)
class CategoryMealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'categorymeal')
    list_display_links = ('id', 'name',)
    list_filter = ('category', 'categorymeal')
    search_fields = ('name', 'category', 'categorymeal',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user',)
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'user', 'name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_ordered', 'complete')
    list_display_links = ('id', 'customer',)
    list_filter = ('date_ordered', 'complete')
    search_fields = ('customer', 'date_ordered',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'order',)
    list_display_links = ('id', 'product',)
    search_fields = ('product', 'order', 'date_added',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'publish',)
