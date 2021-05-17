from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;


@register.filter(name='price_total')
def price_total(product  , cart):
    que = cart_quantity(product  , cart)
    rangemin2 = product.rangemax1 + 1
    rangemin3 = product.rangemax2 + 1
    if que>=product.rangemin1 and que<=product.rangemax1:
        product.price = product.price1
    elif que>=rangemin2 and que<=product.rangemax2:
        product.price = product.price2
    elif que>=rangemin3 and que<=product.rangemax3:
        product.price = product.price3
    return product.price * cart_quantity(product , cart)

@register.filter(name='price_totalp')
def price_totalp(product  , cart):
    que = cart_quantity(product  , cart)
    rangemin2 = product.rangemax1 + 1
    rangemin3 = product.rangemax2 + 1
    if que>=product.rangemin1 and que<=product.rangemax1:
        product.price = product.price1
    elif que>=rangemin2 and que<=product.rangemax2:
        product.price = product.price2
    elif que>=rangemin3 and que<=product.rangemax3:
        product.price = product.price3
    return product.price

@register.filter(name='total_cart_price')
def total_cart_price(products , cart):

    shipcharge = 150 ;
    totalprice = 0;
    for p in products:
        totalprice += price_total(p , cart)
    gst = totalprice*18/100
    finalprice = shipcharge + gst + totalprice
    return int(finalprice)


@register.filter(name='gstprice')
def gstprice(products , cart):

    totalprice = 0;
    for p in products:
        totalprice += price_total(p , cart)
    gst = totalprice*18/100
    return int(gst)

@register.filter(name='givenamed')
def givenamed(invoice, name):
    print(invoice.name)
    return invoice.name
