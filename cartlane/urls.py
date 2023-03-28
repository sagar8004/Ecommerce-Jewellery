"""cartlane URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', views.Master, name='master'),
    path('', views.Index, name='index'),

    path('signup', views.signup, name='signup'),
    path('account/',include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),


    # AddToCart    
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
    
    # ProductDetails
    path('category/<str:id>', views.category, name='category'),
    path('product/<str:id>',views.product_details,name='product_detail'),


    # Inventory
    path('inventory_login', views.inventory_login, name='inventory_login'),
    path('inventory',views.inventory, name='inventory'),
    path('inventory_add',views.inventory_add, name='inventory_add'),
    path('inventory_update/<int:id>',views.inventory_update, name='inventory_update'),
    path('inventory_delete/<int:id>',views.inventory_delete, name='inventory_delete'),
    
    
    # Diamond
    path('diamond', views.diamond, name='diamond'),
    path('diamond_add', views.diamond_add, name='diamond_add'),
    path('diamond/<str:id>',views.diamond_details,name='diamond_detail'),
    path('diamond_update/<str:id>',views.diamond_update,name='diamond_update'),
    path('diamond_delete/<str:id>',views.diamond_delete,name='diamond_delete'),
    
    
    # Search
    path('search/',views.search,name='search'),
    
    
    
    




] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
