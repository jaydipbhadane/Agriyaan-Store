from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Invoice(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    finalprice = models.IntegerField(default=0)
    toalprice = models.IntegerField(default=0)
    gst = models.IntegerField(default=0)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    zipcode = models.CharField(max_length=50, default='', blank=True)
    name = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)


    @staticmethod
    def get_invoice_by_customer(customer_id):
        return Invoice.objects.filter(customer=customer_id).order_by('-date')