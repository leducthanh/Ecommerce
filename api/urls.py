from django.urls import path
from .views import ProductAPIView, ProductDetailAPIView
app_name = 'api'
urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='api'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='api'),
]
