# Generated by Django 3.1 on 2020-08-28 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0003_address_address_line2'),
        ('orders', '0003_auto_20200827_0755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_address', to='addresses.address'),
        ),
    ]
