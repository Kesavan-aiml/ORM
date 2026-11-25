from django.db import models
from django.contrib import admin

class Zomato(models.Model):
    restaurant_id = models.IntegerField()
    customer_id = models.IntegerField()
    food_name = models.CharField(max_length=100)
    food_price = models.IntegerField()
    rating = models.FloatField()

class ZomatoAdmin(admin.ModelAdmin):
    list_display = ('restaurant_id', 'customer_id',
                    'food_name', 'food_price', 'rating')