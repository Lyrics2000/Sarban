# Generated by Django 3.1 on 2020-08-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200823_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product_description',
            new_name='product_full_description',
        ),
        migrations.AddField(
            model_name='products',
            name='product_overview',
            field=models.CharField(default='This is a product overview', max_length=100),
            preserve_default=False,
        ),
    ]
