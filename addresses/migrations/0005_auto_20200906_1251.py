# Generated by Django 3.1 on 2020-09-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0004_deliverytime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverytime',
            name='time',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
