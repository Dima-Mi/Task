from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'sales_api'

urlpatterns = [
    path('products/', views.ProductListApiView.as_view()),
    path('products/<pk>/', views.products_detail),
    path('store/', views.StoreListApiView.as_view()),
    path('store/<pk>/', views.store_detail),
    path('catalog/', views.CatalogListApiView.as_view()),
    path('catalog/<pk>/', views.catalog_detail),
    path('category/', views.CategoryListApiView.as_view()),
    path('warehouse/', views.WarehouseListApiView.as_view()),
]
