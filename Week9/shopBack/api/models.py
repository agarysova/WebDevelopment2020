# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    pass

    def to_json(self):
        return {
            'category_id': self.id,
            'name': self.name,
        }


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(default='')
    count = models.IntegerField()
    category_id = models.ForeignKey(Category, related_name='category_id', on_delete=models.CASCADE, default=1)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category_id': self.category_id_id
        }
