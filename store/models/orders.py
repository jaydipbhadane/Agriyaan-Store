from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    GENDER_CHOICES = (
        ('Ordered', 'Ordered'),
        ('Packed', 'Packed'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered')
    )

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    zipcode = models.CharField(max_length=50, default='', blank=True)
    name = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.CharField(choices=GENDER_CHOICES, max_length=128, default='Ordered')
    track = models.CharField(max_length=50, default='Warehouse Jaipur, RJ', blank=True)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')



