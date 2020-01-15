from django.db import models

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('DRY_PRODUCE', 'DRY_PRODUCE'),
        ('WET_PRODUCE', 'WET_PRODUCE'),
        ('CANNED_FOOD', 'CANNED_FOOD'),
        ('FROZEN', 'FROZEN'),
        ('DAIRY', 'DAIRY'),
        ('BREAD', 'BREAD'),
        ('CEREAL', 'CEREAL'),
        ('BEVERAGE', 'BEVERAGE'),
        ('SNACK', 'SNACK'),
        ('BAKING', 'BAKING'),
        ('CONDIMENTS','CONDIMENTS'),
        ('MEAT', 'MEAT'),
        ('NUT','NUT'),
    ]
    name = models.CharField(max_length=100)
    product_type = models.CharField(
        max_length=15,
        choices=PRODUCT_TYPE_CHOICES,
        default='DRY_PRODUCE'
        )
    price = models.IntegerField()
    quantity =  models.IntegerField()
    product_image = models.ImageField()