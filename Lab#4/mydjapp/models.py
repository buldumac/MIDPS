from django.db import models
from django.contrib import admin

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length = 150)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, related_name="products", default=1)

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title

class History(models.Model):




    def __str__(self):
        return self.title