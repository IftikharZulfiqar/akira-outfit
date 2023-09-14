from django.db import models

# Create your models here.

Category_choices=(
    ('SS','Sports Shirts'),
    ('RS','Regular Shirts'),
    ('TR','Trousers'),
    ('ST','Sports Trouser'),                    
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default="")
    prodapp = models.TextField(default="")
    category = models.CharField(choices=Category_choices,max_length=2)
    product_image = models.ImageField(upload_to='product')


def __str__(self):
        return self.title
