from django.contrib import admin

# Register your models here.

from make_pizzas.models import Pizza, Toppings

admin.site.register(Pizza)
admin.site.register(Toppings)
