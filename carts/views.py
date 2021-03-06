from django.shortcuts import render, redirect
from .models import Cart
from accounts.forms import LoginFrom
from products.models import Product
from orders.models import Order
# Create your views here.
def cart(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/index.html",{'cart' : cart_obj})

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id = product_id)
        except :
            return redirect("cart:cart")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
    return redirect("cart:cart")
def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:cart")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart = cart_obj)
    user=request.user
    billing_profile = None
    login_from = LoginFrom()
    if user.is_authenticated:
        billing_profile = None
    context = {
    'object':order_obj,
    'billing_profile':billing_profile,
    'login_from':login_from
    }
    return render(request, "carts/checkout.html", context)
