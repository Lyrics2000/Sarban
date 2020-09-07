# Generated by Django 3.1 on 2020-09-06 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0006_auto_20200906_1259'),
        ('orders', '0006_auto_20200905_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses.deliverytime'),
        ),
    ]