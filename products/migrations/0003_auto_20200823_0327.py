# Generated by Django 3.1 on 2020-08-23 00:27

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200823_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(null=True, upload_to=products.models.upload_image_path2),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_Image_Field',
            field=models.ImageField(null=True, upload_to=products.models.upload_image_path),
        ),
    ]
