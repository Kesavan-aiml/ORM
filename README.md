# Ex02 Django ORM Web Application
## Date: 25/11/2026

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
admin.py:

from django.contrib import admin
from .models import Zomato, ZomatoAdmin

admin.site.register(Zomato, ZomatoAdmin)

models.py:

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

~~~


## OUTPUT
![alt text](<Screenshot 2026-11-25 182818.png>)


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
