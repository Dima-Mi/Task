from django.conf import settings
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self, ):
        return reverse('sales:product_list_by_category', args=[self.slug])


class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    address = models.SlugField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self, ):
        return reverse('sales:warehouse_detail', args=[self.slug])


class Store(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    description = models.TextField(blank=True)
    contact = models.CharField(max_length=200)
    warehouse = models.ManyToManyField(Warehouse, related_name='warehouse_store')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self, ):
        return reverse('sales:store_detail', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products_category', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='products_store', on_delete=models.CASCADE)
    warehouse = models.ManyToManyField(Warehouse, through='Catalog')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self, ):
        return reverse('sales:product_detail', args=[self.id, self.slug])


class Catalog(models.Model):
    STATUS_OF_SALE = (
        ('available', 'Available'),
        ('sold', 'Sold'),
    )
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_OF_SALE, default='available')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-status', 'updated')
