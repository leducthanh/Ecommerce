from django.urls import path
from products.views import ProductListView, ProductDetailView, ProductAPIView, ProductDetailAPIView
app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('api/', ProductAPIView.as_view(), name='api'),
    path('api/<int:id>/', ProductDetailAPIView.as_view(), name='api'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
]
