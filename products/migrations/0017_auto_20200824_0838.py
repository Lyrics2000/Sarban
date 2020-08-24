# Generated by Django 3.1 on 2020-08-24 05:38

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_moreproductquantirty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moreproductquantirty',
            old_name='product',
            new_name='product_more',
        ),
        migrations.AlterField(
            model_name='moreproductquantirty',
            name='more_product_quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='more_images',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
    ]
