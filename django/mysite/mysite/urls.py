"""mysite URL Configuration

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
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from myapp.views import demo, create_blog, delete_blog, list_blogs, update_blog
from amazon.views import create_inventory, list_inventory, add_to_cart, remove_from_cart,home_page, create_new_user, login_user, logout_user,cart_details



urlpatterns = [
    path('', home_page,name='home'),
    path('admin/', admin.site.urls),
    path('demo',csrf_exempt(demo),name='calculate'),
    path('blogs/create', create_blog,name='create'),
    path('blogs/<int:pk>/delete', delete_blog),
    path('blogs/list',list_blogs), 
    path('blogs/<int:pk>/update', update_blog),
    path('Amazon/create_inventory', create_inventory, name='create_inv' ) ,
    path('Amazon/list_inventory', list_inventory,name='list_inventory'),
    path('Amazon/<int:pk>/AddToCart', add_to_cart),
    path('Amazon/<int:pk>/RemoveFromCart', remove_from_cart),
    path('Amazon/CreateUser', create_new_user, name='register'),
    path('Amazon/LoginUser', login_user, name='LoginUser'),
    path('Amazon/LogOut', logout_user, name='LogOut'),
    path('Amazon/Cart', cart_details, name='cart'),


]
