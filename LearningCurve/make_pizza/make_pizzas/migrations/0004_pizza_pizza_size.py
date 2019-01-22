# Generated by Django 2.1.5 on 2019-01-22 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_pizzas', '0003_auto_20190122_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='pizza_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='M', max_length=1),
        ),
    ]
