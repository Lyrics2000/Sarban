# Generated by Django 3.1 on 2020-08-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200823_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
