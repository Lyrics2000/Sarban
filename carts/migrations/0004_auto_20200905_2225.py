# Generated by Django 3.1 on 2020-09-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.FloatField(blank=True, default=2.0, null=True),
        ),
    ]