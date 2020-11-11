from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
# Create your views here.

from .models import Product
from carts.models import Cart

class ProductListView(ListView):
    template_name = "product/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context

# def product_list_view(request):
#     queryset = Product.objects.all()
#     context = {
#         'object_list':queryset
#     }
#     return render(request, "product/list.html", context)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/detail.html"

    def get_context_data(self,**kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context
    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance

# def product_detail_view(request, slug=None, *args, **kwargs):
#     # queryset = Product.objects.get(pk=pk)
#     queryset = get_object_or_404(Product, slug = slug)
#     context = {
#         'object':queryset
#     }
#     return render(request, "product/detail.html", context)
