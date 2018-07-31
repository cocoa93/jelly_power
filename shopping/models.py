from django.db import models

# Create your models here.
from django.utils import timezone


class Customer(models.Model):
    customer_num = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=10)
    customer_id = models.CharField(max_length=12)
    customer_pw = models.CharField(max_length=15)
    customer_address = models.CharField(max_length=60)
    customer_email = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=11)

class Brand(models.Model):
    brand_num = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=10)
    brand_id = models.CharField(max_length=12)
    brand_pw = models.CharField(max_length=15)
    brand_address = models.CharField(max_length=60)
    brand_email = models.CharField(max_length=30)
    brand_phone = models.CharField(max_length=11)


class Product(models.Model):
    product_num = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=20)
    product_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_price = models.IntegerField() # 가격 최대 50만원

class Order(models.Model):
    #STATUS = (('wp','waiting_for_payment'),('cp','payment_confirmed'),('pd,''preparing_delivery'),('ow','on_the_way')('ar','arrived'))
    order_num = models.IntegerField(primary_key=True)
    order_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #order_status = models.CharField(choices=STATUS)


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=15)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title






