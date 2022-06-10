from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Kx72tLL9eLnz7MyOpxUumE4YnrY3lg8uxVviz7uPYeLDdMk6d4r6tninqClLfzlsDSe8YhteAK4WrkSY9iyJZvp00Tn60WxTG',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)