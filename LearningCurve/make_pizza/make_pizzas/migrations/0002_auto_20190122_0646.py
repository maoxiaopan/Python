# Generated by Django 2.1.5 on 2019-01-22 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('make_pizzas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza_name',
            new_name='text',
        ),
    ]
