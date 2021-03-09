from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'sales'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('store/<slug:slug>', views.store_detail, name='store_detail'),
    path('warehouse/<slug:slug>', views.warehouse_detail, name='warehouse_detail'),
]
