from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.templatetags.cart import price_total, price_totalp, total_cart_price, cart_quantity, gstprice
from store.models.product import Product
from store.models.orders import Order
from django import template
from store.models.invoice import Invoice
from django import template
from store.views.invoice import render_to_pdf
register = template.Library()
class CheckOut(View):

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        zipcode = request.POST.get('zipcode')
        customer = request.session.get('customer')
        cart = request.session.get('cart')

        customer = request.session.get('customer')
        invoices = Invoice.get_invoice_by_customer(customer)

        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=price_totalp(product, cart),
                          address=address,
                          phone=phone,
                          name=name,
                          zipcode=zipcode,
                          quantity=cart.get(str(product.id)))
            order.save()
            customer = request.session.get('customer')
            invoices = Invoice.get_invoice_by_customer(customer)
            invoices.delete()
        for product in products:
            print(cart.get(str(product.id)))
            invoice = Invoice(customer=Customer(id=customer),
                          product=product,
                          price=price_totalp(product, cart),
                          finalprice = price_total(product  , cart),
                          toalprice = total_cart_price(products , cart),
                          gst = gstprice(products , cart),
                          address=address,
                          phone=phone,
                          name=name,
                          zipcode=zipcode,
                          quantity=cart.get(str(product.id)))

            invoice.save()
        request.session['cart'] = {}

        return redirect('invoice')
