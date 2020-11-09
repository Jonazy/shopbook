from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.carts import Cart


# Create your views here.

def order_create(request):
    cart = Cart(request)
    order_form = OrderCreateForm()
    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            for item in cart:
                if request.user.is_authenticated:
                    OrderItem.objects.create(order=order, book=item['book'],
                                            price=item['price'],
                                            quantity=item['quantity'])
                else:
                    return redirect('/accounts/login/')
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
        else:
            order_form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'order_form': order_form, 'cart': cart})
