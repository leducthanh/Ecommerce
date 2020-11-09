"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from ecommerce import views
from accounts.views import login_page, logout_page, register_page

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', login_page, name='login'),
    path('logout/',logout_page, name='logout'),
    path('register/', register_page, name='register'),
    path('admin/', admin.site.urls, name='admin'),
    path('products/', include('products.urls',namespace='produts')),
    path('search/', include('search.urls',namespace='search')),
    path('cart/', include('carts.urls',namespace='cart')),
]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
