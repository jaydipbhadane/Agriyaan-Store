from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)

    price = models.IntegerField(default=0)
    rangemin1 = models.IntegerField(default=1)
    rangemax1 = models.IntegerField(default=0)
    price1 = models.IntegerField(default=0)

    # rangemin2 = models.IntegerField(default=0)
    rangemax2 = models.IntegerField(default=0)
    price2 = models.IntegerField(default=0)

    # rangemin3 = models.IntegerField(default=0)
    rangemax3 = models.IntegerField(default=0)
    price3 = models.IntegerField(default=0)


    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();

