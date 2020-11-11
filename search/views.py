from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView
from products.models import Product
# Create your views here.
class SearchProductView(ListView):
    template_name = "search/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query != None and query != "":
            return Product.objects.search(query)
        return Product.objects.none()
        """
        i : Không phân biệt hoa thường.
        contains : %LIKE%
        exact : mặc định.
        """
