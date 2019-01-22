from django.db import models

# Create your models here.
class Pizza(models.Model):
    PIZZA_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    PIZZA_TYPE = (
        ('PR','Pepperonia'),
        ('CF','Canadian Flavor'),
        ('FS', 'Four Season')
    )
    text = models.CharField(max_length=200)
    Pizza_Size = models.CharField(max_length=1,choices=PIZZA_SIZE, default='M')
    Pizza_Flavor = models.CharField(max_length=2, choices=PIZZA_TYPE, default='CF')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.text

class Toppings(models.Model):
    TOPPING_ITEMS=(
        ('A', 'Apple'),
        ('O', 'Orange'),
        ('I', 'IceCream'),
    )
    pizza = models.ForeignKey(Pizza, on_delete= True)
    text = models.TextField()
    Topping_Choice = models.CharField(max_length=1, choices=TOPPING_ITEMS, default='A')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return self.text




