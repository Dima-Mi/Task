from django.contrib import admin
from .models import Category, Warehouse, Store, Product, Catalog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'contact']
    list_filter = ['warehouse']
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'address']
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'price', 'category', 'store', 'created']
    list_filter = ['store', 'category', 'warehouse']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Catalog)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['products', 'warehouse', 'status', 'updated']
    list_filter = ['warehouse']
    list_editable = ['status']
    ordering = ('status',)
